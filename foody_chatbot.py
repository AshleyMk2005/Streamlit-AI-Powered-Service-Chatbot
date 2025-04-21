import streamlit as st

st.set_page_config(page_title="Foody Chatbot", page_icon="🍛")

# Sample menu with pricing (no images)
dhaba_menu = {
    "Starters": {
        "Paneer Tikka": {"price": 180},
        "Chicken Malai Tikka": {"price": 220},
        "Veg Pakora": {"price": 100},
        "Seekh Kebab": {"price": 200}
    },
    "Main Course": {
        "Butter Chicken": {"price": 250},
        "Dal Makhani": {"price": 150},
        "Shahi Paneer": {"price": 200},
        "Rogan Josh": {"price": 270},
        "Aloo Gobi": {"price": 130}
    },
    "Breads": {
        "Tandoori Roti": {"price": 20},
        "Butter Naan": {"price": 35},
        "Lachha Paratha": {"price": 40}
    },
    "Beverages": {
        "Lassi": {"price": 50},
        "Masala Chai": {"price": 20},
        "Thums Up": {"price": 30}
    },
    "Desserts": {
        "Gulab Jamun": {"price": 60},
        "Kheer": {"price": 70},
        "Ras Malai": {"price": 90}
    }
}

# Bot logic
def get_response(user_input):
    user_input = user_input.lower()

    if any(greet in user_input for greet in ["hello", "hi", "namaste"]):
        return "Namaste! Welcome to Foody, your favorite Punjabi dhaba! 🤗 How can I help you today?"

    if "menu" in user_input:
        return "Here's our dhaba-style menu below 👇"

    if "open" in user_input or "timing" in user_input or "hours" in user_input:
        return "We’re open every day from 10 AM to 11 PM! 🕙🍽️"

    if "where" in user_input or "location" in user_input or "address" in user_input:
        return "📍 Foody is located at Sector 35, Chandigarh.\nMap: https://goo.gl/maps/xyz123"

    if "book" in user_input or "reserve" in user_input or "order" in user_input:
        return "📞 To place an order or reserve a table, call us at +91-9876543210 or WhatsApp the same number!"

    # Check for item query
    for category in dhaba_menu:
        for item in dhaba_menu[category]:
            if item.lower() in user_input:
                price = dhaba_menu[category][item]["price"]
                return f"Yes, we serve {item}! It costs ₹{price}. Would you like to place an order?"

    return "I'm not sure about that, yaar! You can ask me about the menu, timings, or how to order. 😊"

# UI
st.title("🍛 Foody Chatbot")
st.write("Your friendly Punjabi dhaba assistant 🇮🇳")

user_input = st.text_input("Ask me anything about Foody:")

if user_input:
    response = get_response(user_input)
    st.markdown(f"**Bot:** {response}")

# Show full menu below
if "menu" in user_input.lower():
    st.markdown("### 🧾 Our Menu")
    for category, items in dhaba_menu.items():
        st.markdown(f"#### {category}")
        for dish, details in items.items():
            st.markdown(f"**{dish}** - ₹{details['price']}")
