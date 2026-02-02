# MCP-Server-LLM-Tool-Consumer

This project implements a robust bridge between a **Deterministic Core** (Python logic) and a **Probabilistic Brain** (Gemini LLM) using the **Model Context Protocol (MCP)** logic.

## 1. Technical Objective
The goal is to build a reliable microservice (the MCP Server) that performs logic without AI interference, while a smart but erratic LLM (the Client) identifies when to call those functions based on natural language input.

---

## 2. Architecture & Data Flow
The system follows a strict decoupling of responsibilities:

1.  **Discovery**: The Client queries the Server for available tools and resources via `stdio`.
2.  **Planning**: The Client passes the user's prompt and the tool's JSON schema to Gemini.
3.  **Execution**: Gemini returns a tool request; the Client executes it against the Server's deterministic logic.
4.  **Final Response**: The Client returns the raw tool result to the LLM for a natural language summary.

---

## 3. Tool & Resource Definitions

### **Tool: `get_word_stats`**
* **Description**: Analyzes a string to return word count, character count, and complexity.
* **Input Schema**:
    ```json
    {
      "text": "string"
    }
    ```
* **Deterministic Logic**: Pure Python code; no AI calls inside.

### **Resource: `mcp://config/info`**
* **Description**: A static, read-only JSON data source containing system metadata.
* **Data**: Versioning, author (Rashmi Priya), and system status.

---

## 4. Setup and Execution

### **Prerequisites**
* Python 3.10+
* Google Generative AI SDK
    ```bash
    python -m pip install -U google-generativeai
    ```

### **Run Commands**
1.  **Deterministic Test** (The "Remove the LLM" Test):
    Proves the server runs successfully without the LLM.
    ```bash
    python test_server.py
    ```
2.  **Full System Run**:
    Starts the bridge between the LLM and the Server logic.
    ```bash
    python client.py
    ```

---

## 5. Engineering Maturity Features
* **Defensive Validation**: The server validates input types (e.g., ensuring `text` is a string) and returns structured JSON error messages if the LLM hallucinates arguments.
* **Boundary Logging**: Full transparency of data moving between the Client and Server using `INFO:` and `SERVER_LOG:` markers.
* **Decoupled Logic**: The server logic is completely usable without an LLM interface.

---

**Developed by:** Rashmi Priya  (24BCE10054)
**Round:** AI Club’s Tech Team Task Round
