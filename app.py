import streamlit as st
import tempfile
from concurrent.futures import ThreadPoolExecutor

from agents.parser_agent import parse_problem
from agents.router_agent import route_problem
from agents.solver_agent import solve_math_problem
from agents.verifier_agent import verify_solution
from agents.explainer_agent import generate_explanation
from agents.hitl_agent import check_hitl

from rag.retriever import retrieve_math_rules
from memory.memory_store import save_interaction

from tools.ocr import extract_text_from_image
from tools.speech_to_text import transcribe_audio


st.set_page_config(page_title="AI Math Mentor")

st.title("AI Math Mentor")
st.write("Solve JEE-style math problems using AI agents")

mode = st.selectbox(
    "Choose Input Mode",
    ["Text", "Image", "Audio"]
)

question = None


# ------------------------
# TEXT INPUT
# ------------------------

if mode == "Text":

    question = st.text_area("Enter your math question")


# ------------------------
# IMAGE INPUT
# ------------------------

elif mode == "Image":

    uploaded_file = st.file_uploader("Upload math problem image")

    if uploaded_file is not None:

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_file.read())
            image_path = tmp.name

        extracted_text = extract_text_from_image(image_path)

        st.subheader("OCR Extraction Preview")

        question = st.text_area(
            "Edit extracted text if needed",
            extracted_text
        )


# ------------------------
# AUDIO INPUT
# ------------------------

elif mode == "Audio":

    audio_file = st.file_uploader(
        "Upload audio question",
        type=["wav", "mp3", "m4a"]
    )

    if audio_file is not None:

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(audio_file.read())
            audio_path = tmp.name

        transcript = transcribe_audio(audio_path)

        st.subheader("Speech Transcript")

        question = st.text_area(
            "Edit transcript if needed",
            transcript
        )


# ------------------------
# SOLVE BUTTON
# ------------------------

if st.button("Solve Problem"):

    if not question:
        st.warning("Please provide a math question.")

    else:

        executor = ThreadPoolExecutor(max_workers=4)

        trace = []

        st.subheader("Agent Trace")


        # ------------------------
        # Parser Agent
        # ------------------------

        parsed = parse_problem(question)
        trace.append("Parser Agent → Structured problem")


        # ------------------------
        # Router + Retriever (PARALLEL)
        # ------------------------

        router_future = executor.submit(route_problem, parsed)
        retriever_future = executor.submit(retrieve_math_rules, question)

        route = router_future.result()

        retrieval = retriever_future.result()
        docs = retrieval["rules"]

        trace.append(f"Router Agent → {route}")
        trace.append("Retriever → Retrieved math rules")


        # ------------------------
        # Solver Agent
        # ------------------------

        solution = solve_math_problem(question)
        trace.append("Solver Agent → Generated solution")


        # ------------------------
        # Verifier + Explainer (PARALLEL)
        # ------------------------

        verify_future = executor.submit(
            verify_solution,
            question,
            solution
        )

        explain_future = executor.submit(
            generate_explanation,
            question,
            solution
        )

        verification = verify_future.result()
        explanation = explain_future.result()

        trace.append("Verifier Agent → Checked correctness")
        trace.append("Explainer Agent → Generated explanation")


        # ------------------------
        # HITL
        # ------------------------

        decision = check_hitl(parsed, verification)
        trace.append(f"HITL Decision → {decision}")


        # ------------------------
        # Save interaction
        # ------------------------

        save_interaction(question, solution)


        # ------------------------
        # Show Agent Trace
        # ------------------------

        for step in trace:
            st.write("•", step)


        # ------------------------
        # Retrieved Knowledge
        # ------------------------

        st.subheader("Retrieved Knowledge")

        for doc in docs:
            st.write(doc)


        # ------------------------
        # Verification
        # ------------------------

        st.subheader("Verification")

        st.write(verification)


        # ------------------------
        # Confidence Indicator
        # ------------------------

        confidence = "Unknown"

        if "High" in verification:
            confidence = "High"
        elif "Medium" in verification:
            confidence = "Medium"
        elif "Low" in verification:
            confidence = "Low"

        st.subheader("Confidence Indicator")

        if confidence == "High":
            st.success("High confidence")
        elif confidence == "Medium":
            st.warning("Medium confidence")
        else:
            st.error("Low confidence")


        # ------------------------
        # Final Explanation
        # ------------------------

        st.subheader("Final Answer + Explanation")

        st.write(explanation)


        # ------------------------
        # Feedback Buttons
        # ------------------------

        st.subheader("Was the answer correct?")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("✅ Correct"):
                save_interaction(question, solution, "correct")
                st.success("Feedback saved")

        with col2:
            if st.button("❌ Incorrect"):
                save_interaction(question, solution, "incorrect")
                st.warning("Feedback saved")