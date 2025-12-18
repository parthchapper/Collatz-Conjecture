import streamlit as st
import matplotlib.pyplot as plt

# --------------------------------------------
# Page configuration
# --------------------------------------------
st.set_page_config(
    page_title="Collatz Explorer",
    page_icon="📉",
    layout="wide"
)

st.title("📉 Collatz Conjecture Explorer")
st.caption("Recursive testing and visual comparison of Collatz sequences")

# --------------------------------------------
# Recursive Collatz function
# --------------------------------------------
def collatz_recursive(n, sequence=None):
    if sequence is None:
        sequence = [n]

    if n == 1:
        return sequence

    if n % 2 == 0:
        return collatz_recursive(n // 2, sequence + [n // 2])
    else:
        return collatz_recursive(3 * n + 1, sequence + [3 * n + 1])


# --------------------------------------------
# Session state for persistence
# --------------------------------------------
if "all_sequences" not in st.session_state:
    st.session_state.all_sequences = []

if "all_starts" not in st.session_state:
    st.session_state.all_starts = []


# --------------------------------------------
# Sidebar controls
# --------------------------------------------
with st.sidebar:
    st.header("Controls")
    start_value = st.number_input(
        "Starting number",
        min_value=1,
        value=7,
        step=1
    )

    run = st.button("Run Collatz")

    st.markdown("---")
    st.markdown("**Visualization Options**")
    log_scale = st.checkbox("Log-scale Y axis", value=False)


# --------------------------------------------
# Run logic
# --------------------------------------------
if run:
    sequence = collatz_recursive(start_value)
    st.session_state.all_sequences.append(sequence)
    st.session_state.all_starts.append(start_value)


# --------------------------------------------
# Layout: two columns
# --------------------------------------------
col1, col2 = st.columns(2)

# --------------------------------------------
# Single sequence plot
# --------------------------------------------
with col1:
    st.subheader("Single Number Behavior")

    if run:
        fig1, ax1 = plt.subplots(figsize=(6, 4))

        ax1.plot(sequence, linewidth=2.5, marker="o", markersize=4)
        ax1.fill_between(range(len(sequence)), sequence, alpha=0.15)

        ax1.set_title(f"Collatz Sequence for {start_value}")
        ax1.set_xlabel("Step")
        ax1.set_ylabel("Value")
        ax1.grid(True, linestyle="--", alpha=0.4)

        if log_scale:
            ax1.set_yscale("log")

        st.pyplot(fig1)

        st.metric("Steps", len(sequence) - 1)
        st.metric("Peak Value", max(sequence))

    else:
        st.info("Run the sequence to see the plot.")


# --------------------------------------------
# Persistent comparison plot
# --------------------------------------------
with col2:
    st.subheader("All Tested Numbers")

    if st.session_state.all_sequences:
        fig2, ax2 = plt.subplots(figsize=(6, 4))

        for seq, start in zip(
            st.session_state.all_sequences,
            st.session_state.all_starts
        ):
            ax2.plot(seq, alpha=0.65, linewidth=1.6, label=str(start))

        ax2.set_title("Collatz Comparison")
        ax2.set_xlabel("Step")
        ax2.set_ylabel("Value")
        ax2.grid(True, linestyle="--", alpha=0.4)

        if log_scale:
            ax2.set_yscale("log")

        if len(st.session_state.all_sequences) <= 8:
            ax2.legend(title="Start", fontsize=8)

        st.pyplot(fig2)

    else:
        st.info("No sequences yet. Run a number to begin.")


# --------------------------------------------
# Footer
# --------------------------------------------
st.markdown("---")
st.caption(
    "Recursive evaluation • Persistent visualization • Built with Streamlit"
)
