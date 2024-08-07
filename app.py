from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model
with open('laptop_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the dataset to get unique values for each feature
file_path = r"C:\Users\yaswa\OneDrive\Desktop\laptop_price\laptop_PRICE.csv"
data = pd.read_csv(file_path)

@app.route('/', methods=['GET', 'POST'])
def home():
    # Get unique values for each feature
    companies = sorted(data['Company'].unique())
    cpu_brands = sorted(data['Cpu brand'].unique())
    ram_options = sorted(data['Ram'].unique())
    inches_options = sorted(data['Inches'].unique())
    weight_options = sorted(data['Weight'].unique())

    if request.method == 'POST':
        # Get user input from the form
        company = request.form.get('company')
        cpu_brand = request.form.get('cpu_brand')
        ram = float(request.form.get('ram'))
        inches = float(request.form.get('inches'))
        weight = float(request.form.get('weight'))

        # Create a DataFrame with user input
        input_data = pd.DataFrame({
            'Company': [company],
            'Cpu brand': [cpu_brand],
            'Ram': [ram],
            'Inches': [inches],
            'Weight': [weight]
        })

        # Make prediction
        prediction = model.predict(input_data)

        # Round the prediction to 2 decimal places
        predicted_price = round(prediction[0], 2)

        return render_template('index.html', 
                               prediction=predicted_price,
                               companies=companies,
                               cpu_brands=cpu_brands,
                               ram_options=ram_options,
                               inches_options=inches_options,
                               weight_options=weight_options)

    return render_template('index.html', 
                           companies=companies,
                           cpu_brands=cpu_brands,
                           ram_options=ram_options,
                           inches_options=inches_options,
                           weight_options=weight_options)

if __name__ == '__main__':
    app.run(debug=True)