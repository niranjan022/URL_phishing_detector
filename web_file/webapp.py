import streamlit as st
import joblib
import re
import os
import requests



def extract_features(url):
    features = []
    url_str = str(url)
    
    features.append(len(url_str))
   
    specials = ['@','?','-','=','.','#','%','+','$','!','*',',','//']
    for s in specials:
        features.append(url_str.count(s))
   
    from urllib.parse import urlparse
    hostname = str(urlparse(url_str).hostname)
    abnormal = 1 if re.search(hostname, url_str) else 0
    features.append(abnormal)
   
    scheme = urlparse(url_str).scheme
    features.append(1 if scheme == 'https' else 0)
   
    features.append(sum(c.isdigit() for c in url_str))
  
    features.append(sum(c.isalpha() for c in url_str))
  
    shortener_pattern = (
        r'bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
        r'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
        r'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
        r'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
        r'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
        r'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
        r'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
        r'tr\.im|link\.zip\.net'
    )
    features.append(1 if re.search(shortener_pattern, url_str) else 0)
    
    ip_pattern = (
        r'(([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.'
        r'([01]?\d\d?|2[0-4]\d|25[0-5]))|'
        r'((0x[0-9a-fA-F]{1,2})\.(0x[0-9a-fA-F]{1,2})\.(0x[0-9a-fA-F]{1,2})\.(0x[0-9a-fA-F]{1,2}))|'
        r'(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}|'
        r'([0-9]+(?:\.[0-9]+){3}:[0-9]+)|'
        r'((?:(?:\d|[01]?\d\d|2[0-4]\d|25[0-5])\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d|\d)(?:/\d{1,2})?)'
    )
    features.append(1 if re.search(ip_pattern, url_str) else 0)
    return features

st.title("🔐 Phishing URL Detector")
st.write("Enter a URL to check if it’s **Phishing** or **Safe**.")



MODEL_URL = "https://drive.google.com/uc?export=download&id=1mUH2pSrZ94NwwOrBZ4jhh5-OFyVEg3fh"
MODEL_PATH = "RF_model.pkl"

if not os.path.exists(MODEL_PATH):
    with st.spinner("Downloading model..."):
        r = requests.get(MODEL_URL)
        with open(MODEL_PATH, "wb") as f:
            f.write(r.content)

model = joblib.load(MODEL_PATH)

url_input = st.text_input("Enter URL:")



category_map = {
    0: ("Benign", st.success, "✅ This URL looks **Benign** (Safe)"),
    1: ("Defacement", st.warning, "⚠️ This URL looks **Defacement**"),
    2: ("Phishing", st.error, "🚨 This URL looks **Phishing**"),
    3: ("Malware", st.error, "🛑 This URL looks **Malware**"),
}

if st.button("Check URL"):
    if url_input.strip() == "":
        st.warning("Please enter a URL")
    else:
        clean_url = url_input.replace("www.", "")
        features = extract_features(clean_url)
        prediction = model.predict([features])[0]
        label, color_func, message = category_map.get(prediction, ("Unknown", st.info, "❓ Unknown Category"))
        color_func(message)
