# run.py

import os

from web import create_app

app = create_app()
app.secret_key = os.environ.get("SECRET_KEY", "dev")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=False)
