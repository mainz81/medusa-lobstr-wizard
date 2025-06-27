from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

steps = [
    {
        "title": "Step 1: Visit LOBSTR and Start Signup",
        "desc": "Go to <a href='https://lobstr.co' target='_blank'>LOBSTR.co</a> and click <b>“Create Account”</b>.<br>"
                "Enter your email and a strong, unique password.",
        "img": "https://i.imgur.com/g8Q7Wry.png"
    },
    {
        "title": "Step 2: Confirm Your Email",
        "desc": "Check your inbox (and spam folder).<br>"
                "Click the confirmation link LOBSTR sent you.",
        "img": "https://i.imgur.com/fcFxzxG.png"
    },
    {
        "title": "Step 3: Save Your Secret Key & Stellar Address",
        "desc": "Once logged in, <b>write down your Secret Key (starts with S...)</b> and your Stellar Address (starts with G...).<br>"
                "<b>Never share your Secret Key with anyone, ever!</b>",
        "img": "https://i.imgur.com/3dfu7uH.png"
    },
    {
        "title": "Step 4: Fund Your Wallet with XLM",
        "desc": "Buy XLM (Stellar Lumens) on any major crypto exchange (Coinbase, Binance, Kraken, etc).<br>"
                "Send your XLM to your Stellar Address. Double-check the address!",
        "img": "https://i.imgur.com/W8wOnCJ.png"
    },
    {
        "title": "Step 5: Ready to Pay?",
        "desc": "In LOBSTR, click <b>Send</b>, paste Medusa's wallet address, enter your amount (see your contract), and confirm.<br>"
                "Include the correct Memo if required.",
        "img": "https://i.imgur.com/cbC6n5g.png"
    },
    {
        "title": "Step 6: Visual Help & Security",
        "desc": "<a href='https://www.youtube.com/watch?v=WfXR9KceXZE' target='_blank'>Watch the LOBSTR setup video here</a>.<br>"
                "<b>Never share your Secret Key or Recovery Phrase.</b> Use only the official LOBSTR app or website.",
        "img": "https://i.imgur.com/3dcYhIw.png"
    }
]

@app.route("/", methods=["GET", "POST"])
def wizard():
    step = int(request.args.get("step", 0))
    if step >= len(steps):
        return redirect(url_for("complete"))
    if request.method == "POST":
        return redirect(url_for("wizard", step=step + 1))
    return render_template_string("""
        <html><head>
            <title>Medusa LOBSTR Wallet Wizard</title>
            <style>
                body { font-family: 'Segoe UI', Arial, sans-serif; background: #19191a; color: #eaeaea; }
                .wizard-box { max-width: 500px; margin: 50px auto; background: #232326; border-radius: 18px; padding: 36px; box-shadow: 0 0 28px #000b; }
                h2 { color: #ffe066; margin-bottom: 14px;}
                img { max-width: 400px; border-radius: 12px; margin: 18px 0; box-shadow: 0 2px 12px #111b;}
                button { background: #ffe066; border: none; padding: 12px 24px; color: #19191a; border-radius: 7px; font-weight: bold; font-size: 1.15em; margin-top: 20px;}
                a { color: #73e6d7; text-decoration: underline;}
            </style>
        </head><body>
            <div class="wizard-box">
                <h2>{{ step_data.title }}</h2>
                <div>{{ step_data.desc|safe }}</div>
                <img src="{{ step_data.img }}" alt="Step Screenshot"/>
                <form method="post">
                    <button type="submit">{% if last %}Finish{% else %}Next Step ➔{% endif %}</button>
                </form>
                <div style="margin-top:18px;">
                    Step {{ step+1 }} of {{ total_steps }}
                </div>
            </div>
        </body></html>
    """, step_data=steps[step], step=step, last=(step==len(steps)-1), total_steps=len(steps))

@app.route("/complete")
def complete():
    return render_template_string("""
        <html><head><title>Wizard Complete</title></head>
        <body style="background:#19191a;color:#ffe066;font-family:'Segoe UI',Arial,sans-serif;">
        <div style="max-width:500px;margin:80px auto;background:#232326;border-radius:18px;padding:38px;box-shadow:0 0 24px #000c;">
            <h2>Serpent Salute! 🐍</h2>
            <p>You have completed Medusa's LOBSTR Wallet setup ritual.<br>
            Now you're ready for legendary Subinac deals.<br><br>
            <a href='https://lobstr.co' target='_blank'>Go to LOBSTR Wallet</a><br>
            <a href='https://www.youtube.com/watch?v=WfXR9KceXZE' target='_blank'>View Step-by-Step Video</a>
            </p>
        </div>
        </body></html>
    """)

# Do NOT use `if __name__ == "__main__"` for Render deployment.
# Render will auto-detect app = Flask(__name__) for Gunicorn!

