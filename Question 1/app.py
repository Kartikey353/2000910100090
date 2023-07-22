from flask import Flask, jsonify , request
import requests
app = Flask(__name__) 



@app.route('/numbers', methods=['GET'])
def get_numbers():
    try:
        url_list = request.args.getlist('url')

        if not url_list:
            return jsonify({'error': 'No URLs provided'}), 400

        combined_numbers = []

        for url in url_list:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                numbers = data.get('numbers', [])
                combined_numbers.extend(numbers)
            else:
                return jsonify({'error': f'Failed to fetch data from URL: {url}'}), 500

        # Sort the combined numbers list in ascending order and remove duplicates
        combined_numbers = sorted(set(combined_numbers))

        return jsonify({'numbers': combined_numbers})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
 
if __name__ == '__main__':
    app.run(debug=True)