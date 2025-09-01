#!/usr/bin/env python3
"""
Utility script to stop any running documentation flow processes and clear user input session
"""
import os
import sys
import signal
import psutil
import json

def find_and_stop_processes():
    """Find and stop any Python processes running the documentation flow"""
    stopped_processes = []
    
    try:
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                cmdline = proc.info['cmdline']
                if cmdline and any('documentazione_flow' in arg or 'main.py' in arg for arg in cmdline):
                    print(f"🔍 Found process: PID {proc.info['pid']} - {' '.join(cmdline)}")
                    proc.terminate()
                    stopped_processes.append(proc.info['pid'])
                    print(f"🛑 Terminated process {proc.info['pid']}")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
    except Exception as e:
        print(f"❌ Error searching for processes: {e}")
    
    return stopped_processes

def clear_user_input_session():
    """Clear any existing user input session data"""
    try:
        # Clear the global variables in user_input_tool module
        print("🧹 Clearing user input session data...")
        
        # This will be cleared when the module is reloaded
        session_file = os.path.join(os.path.dirname(__file__), 'temp_session.json')
        if os.path.exists(session_file):
            os.remove(session_file)
            print(f"🗑️  Removed temporary session file: {session_file}")
        
        print("✅ User input session data cleared")
    except Exception as e:
        print(f"⚠️  Warning clearing session data: {e}")

def show_recommendations():
    """Show recommendations to prevent the loop issue"""
    print("\n" + "="*80)
    print("💡 RACCOMANDAZIONI PER EVITARE LOOP FUTURI")
    print("="*80)
    print("1. 🔄 Usa il tool 'reset_user_input_session' prima di iniziare nuove sessioni")
    print("2. ⏭️  Rispondi 'skip' per saltare domande ripetitive")
    print("3. 🚫 Usa 'Non disponibile' per informazioni che non hai")
    print("4. 💾 Il sistema ora ricorda le risposte date per evitare duplicati")
    print("5. 📊 Usa 'get_session_summary' per vedere le risposte già raccolte")
    print("="*80)

def main():
    """Main function to stop loop and provide recommendations"""
    print("🚨 DOCUMENTAZIONE FLOW - STOP LOOP UTILITY")
    print("="*60)
    
    # Find and stop processes
    stopped = find_and_stop_processes()
    
    if stopped:
        print(f"✅ Stopped {len(stopped)} processes: {stopped}")
    else:
        print("ℹ️  No documentation flow processes found running")
    
    # Clear session data
    clear_user_input_session()
    
    # Show recommendations
    show_recommendations()
    
    print("\n🎯 Il sistema è ora pronto per una nuova esecuzione senza loop!")
    print("🚀 Puoi riavviare il processo di documentazione.")

if __name__ == "__main__":
    main()
