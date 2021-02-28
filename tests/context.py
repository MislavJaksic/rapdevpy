import os
import sys

# Adds "rapdevpy" to sys.path
# Now you can do import with "from rapdevpy.Sub-Package ..."
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "rapdevpy"))
)
