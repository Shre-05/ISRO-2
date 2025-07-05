from crawl_faq import get_faq_data

faq_data = get_faq_data()

def keyword_bot(query):
    query = query.lower().strip()

    if "purpose of mosdac" in query or "main purpose of mosdac" in query or "what is mosdac" in query:
        return "MOSDAC provides satellite data products for ocean, land, and atmosphere applications."

    elif "how to access mosdac" in query or "how can i access mosdac" in query or "access data" in query:
        return "To access MOSDAC data, users need to sign up on the portal and log in to download available satellite products."

    elif "is mosdac data free" in query or "free to use" in query or "mosdac data cost" in query:
        return "Yes, MOSDAC data is free for academic and research purposes. Just register and you can access it."

    elif "what information is available" in query or "what data does mosdac provide" in query or "information on mosdac" in query:
        return "MOSDAC provides data from Indian satellites related to rainfall, ocean wind, cloud motion, temperature, humidity, and more — useful for climate, agriculture, ocean, and disaster monitoring."

    for faq in faq_data:
        if any(word in faq.lower() for word in query.split()):
            return faq

    return "❌ Sorry, I couldn’t find an answer. Try rephrasing?"

