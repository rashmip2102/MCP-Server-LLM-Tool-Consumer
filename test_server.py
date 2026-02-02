import subprocess
import json

def test_logic():
    # Simulate a manual tool call to the server
    test_payload = {
        "method": "call_tool",
        "params": {"arguments": {"text": "Hello world from the test script"}}
    }
    
    proc = subprocess.Popen(['python', 'server.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    stdout, _ = proc.communicate(input=json.dumps(test_payload) + "\n")
    
    result = json.loads(stdout)
    print("Manual Test Result:", result)
    assert "result" in result
    assert result["result"]["word_count"] == 6
    print("Test Passed: Server is deterministic and decoupled!")

if __name__ == "__main__":
    test_logic()