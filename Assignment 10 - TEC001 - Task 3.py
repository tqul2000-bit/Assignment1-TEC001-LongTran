from flask import Flask
import math

app = Flask(__name__)

@app.route('/prime_number/<int:number>')

def prime_number(number):
    ans = is_prime_number(number)
    response = {
        'Number': number,
        'isPrime': ans
    }
    return response
def is_prime_number(number):
    num = int(number)
    if num == 2:
        return True
    if num < 2:
        return False
    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)