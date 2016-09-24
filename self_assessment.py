import dondash
import os

reporter = dondash.SecurityReporter()
agent_id = os.getenv("AGENT_ID")

reporter.scan_all_modules(agent_id)
