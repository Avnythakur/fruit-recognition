import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image


#custom styling
st.markdown(
    """
    <style>

    .title {
        font-size: 38px;
        font-weight: bold;
        text-align: center;
        color: #2E86C1;
    }
    .subtitle {
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        color: #2874A6;
    }
    .prediction {
        font-size: 20px;
        font-weight: bold;
        color: #148F77;
    }
    .sidebar-title {
        font-size: 24px;
        font-weight: bold;
        color: #1C2833;
    }
    .dataset-info {
        font-size: 18px;
        color: #1F618D;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

#tensorflow model prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model('trained_model.keras')
    image = Image.open(test_image).convert('RGB')
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(64,64))
    input_array = tf.keras.preprocessing.image.img_to_array(image)
    input_array = np.array([input_array])
    predictions = model.predict(input_array)
    return np.argmax(predictions)
    

                                               
    
#sidebar
# st.sidebar.markdown("<p class='sidebar-title'>Dashboard</p>", unsafe_allow_html=True)
st.sidebar.markdown(
    """
    <h2 style='text-align: center; font-size: 28px; font-weight: bold;'>
    📊 Dashboard
    </h2>
    """,
    unsafe_allow_html=True
)

app_mode = st.sidebar.radio("Select Page", ['🏠 Home', '📌 About Project', '🔍 Prediction'])

# st.sidebar.header("Dashboard")
# app_mode = st.sidebar.selectbox("Select Page", ['Home','About Project','Prediction'])


## main page
if app_mode == "🏠 Home":
    st.markdown(
        """
        <h1 style='text-align: center; font-size: 45px; font-weight: bold; color: #2E86C1;'>
        🍎 Fruits & Vegetables Recognition System 🥦
        </h1>
        """,
        unsafe_allow_html=True
    )

    # st.markdown("<p class='title'>🍎 Fruits & Vegetables Recognition System 🥦</p>", unsafe_allow_html=True)
    st.image('background_image.png', use_container_width=True)


elif app_mode == '📌 About Project':
    st.markdown("<p class='title' style='font-size:40px;'>About Project</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'style='font-size:28px;'>About Dataset</p>", unsafe_allow_html=True)
    st.markdown("<p class='dataset-info'>This dataset contains images of the following food items:</p>", unsafe_allow_html=True)
    
    st.code("""
    Fruits - Banana, Apple, Pear, Grapes, Orange, Kiwi, Watermelon, 
    Pomegranate, Pineapple, Mango
    """)
    st.code("""
    Vegetables - Cucumber, Carrot, Capsicum, Onion, Potato, Lemon, Tomato, 
    Radish, Beetroot, Cabbage, Lettuce, Spinach, Soybean, Cauliflower, 
    Bell Pepper, Chilli Pepper, Turnip, Corn, Sweetcorn, Sweet Potato, 
    Paprika, Jalapeño, Ginger, Garlic, Peas, Eggplant
    """)

    st.markdown("<p class='subtitle'style='font-size: 28px;'>Dataset Structure</p>", unsafe_allow_html=True)
    st.markdown("""
    - **Train:** Contains 100 images per category.  
    - **Test:** Contains 10 images per category.  
    - **Validation:** Contains 10 images per category.  
    """, unsafe_allow_html=True)


elif app_mode == '🔍 Prediction':
    st.markdown("<p class='title'style='font-size: 36px;'>Model Prediction</p>", unsafe_allow_html=True)
    test_image = st.file_uploader('📷 Upload an Image:', type=['png', 'jpg', 'jpeg'])

    if test_image:
        st.image(test_image, caption="Uploaded Image", use_container_width=True)  # UPDATED

        if st.button("🔍 Predict"):
            result_index = model_prediction(test_image)

            if result_index is None:
                st.error("⚠️ No image uploaded! Please upload an image first.")
            else:
                # Reading labels
                with open('labels.txt') as f:
                    label = [line.strip() for line in f.readlines()]

                st.markdown(f"<p class='prediction'>✅ Model predicts: <b>{label[result_index]}</b></p>", unsafe_allow_html=True)




# if(app_mode=="Home"):
#     st.header("Fruits & Vegetables Recognition System")
#     image_path = 'background_image.png'
#     st.image(image_path)


# ## About Project
# elif(app_mode=='About Project'):
#     st.header("About Project")
#     st.subheader("About Dataset")
#     st.text("This Dataset contains the image of following food items:")
#     st.code("Fruits - Banana, Apple, Pear, Grapes, Orange, Kiwi, Watermelon, Pomegranate, Pineapple, Mango")
#     st.code('Vegetables - Cucumber, Carrot, Capsicum, Onion, Potato, Lemon, Tomato, Radish, Beetroot, Cabbage, Lettuce, Spinach, Soybean, Cauliflower, Bell Pepper, Chilli Pepper, Turnip, Corn, Sweetcorn, Sweet Potato, Paprika, Jalapeño, Ginger, Garlic, Peas, Eggplant')
#     st.subheader('Content')
#     st.text('This dataset contains three folders:')
#     st.text('1. Train: Contains 100 images per category.')
#     st.text('2. Test: Contains 10 images per category.')
#     st.text('3. Validation: Contains 10 images per category.')

# ## Prediction Page
# elif(app_mode=='Prediction'):
#     st.header("Model Prediction")
#     test_image = st.file_uploader('Choose an Image:')
#     if(st.button('Show Image')):
#         st.image(test_image)
#     # predict button
#     if(st.button("Predict")):
#         st.write("Our Prediction")
#         result_index = model_prediction(test_image)
#         #Reading labels
#         with open('labels.txt') as f:
#             content = f.readlines()
#         label = []
#         for i in content:
#             label.append(i[:-1])
#         st.success("Model is Predicting it's a {}".format(label[result_index]))







            
