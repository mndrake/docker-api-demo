"""
basic flask-restplus api example
"""
import credit_model

if __name__ == "__main__":
    credit_model.app.run(host='0.0.0.0', port=3000)
