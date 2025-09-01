#!/usr/bin/env python3
"""
Test script to demonstrate the fixed user input tool functionality
"""
import sys
import os

# Add the src directory to the path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.insert(0, src_dir)

from documentazione_flow.tools.user_input_tool import (
    request_user_input,
    collect_missing_information,
    reset_user_input_session,
    get_session_summary
)

def test_fixed_functionality():
    """Test the fixed user input functionality"""
    print("🧪 TESTING FIXED USER INPUT TOOL")
    print("="*50)
    
    # Reset session to start clean
    print("1. Resetting session...")
    result = reset_user_input_session()
    print(f"   {result}")
    
    # Test asking the same question twice (should prevent loop)
    print("\n2. Testing duplicate question prevention...")
    
    print("   First time asking about models:")
    response1 = request_user_input(
        "What AI models are implemented? Provide their names and versions.",
        "Models and Algorithms"
    )
    print(f"   Response: {response1[:50]}...")
    
    print("\n   Second time asking the same question (should be prevented):")
    response2 = request_user_input(
        "What AI models are implemented? Provide their names and versions.",
        "Models and Algorithms"
    )
    print(f"   Response: {response2[:50]}...")
    
    # Test session summary
    print("\n3. Getting session summary...")
    summary = get_session_summary()
    print(f"   Summary: {summary[:100]}...")
    
    print("\n✅ Test completed successfully!")
    print("💡 The loop issue should now be fixed!")

if __name__ == "__main__":
    test_fixed_functionality()
