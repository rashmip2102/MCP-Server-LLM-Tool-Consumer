from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format="[SERVER] %(message)s")

# ---------- Resource ----------
RESOURCE_CONFIG = {
    "name": "Text Analyzer MCP",
    "version": "1.0",
    "rules": "Deterministic tools only. No AI."
}

# ---------- Tool Schema ----------
TOOL_SCHEMA = {
    "name": "analyze_text",
    "description": "Analyze text and return counts",
    "input_schema": {
        "type": "object",
        "properties": {
            "text": {"type": "string"}
        },
        "required": ["text"]
    },
    "output_schema": {
        "type": "object",
        "properties": {
            "word_count": {"type": "integer"},
            "char_count": {"type": "integer"},
            "line_count": {"type": "integer"}
        }
    }
}

# ---------- Tool Logic ----------
def analyze_text(args):
    if "text" not in args:
        logging.warning("Hallucination Detected: Missing 'text'")
        return {"error": "Missing required field 'text'"}

    if not isinstance(args["text"], str):
        logging.warning("Hallucination Detected: Invalid type for 'text'")
        return {"error": "Invalid type for 'text'"}

    text = args["text"]
    return {
        "word_count": len(text.split()),
        "char_count": len(text),
        "line_count": len(text.splitlines()) or 1
    }

# ---------- MCP Endpoints ----------
@app.route("/tools", methods=["GET"])
def list_tools():
    return jsonify([TOOL_SCHEMA])

@app.route("/resources", methods=["GET"])
def list_resources():
    return jsonify({"file://config": RESOURCE_CONFIG})

@app.route("/call", methods=["POST"])
def call_tool():
    data = request.json
    if data.get("tool") != "analyze_text":
        return jsonify({"error": "Unknown tool"}), 400

    result = analyze_text(data.get("args", {}))
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=8000)
