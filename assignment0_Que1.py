{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cb0f6f7a-7724-4117-b3cb-dee7b99b9f29",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter coeff of cubic terms 1\n",
      "enter coeff of quadratic term 2\n",
      "enter coeff of linear term 3\n",
      "enter coeff of constant term 4\n",
      "what is the value of x? 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the slope of the cubic polynomial is 10.0\n"
     ]
    }
   ],
   "source": [
    "a = float(input(\"enter coeff of cubic terms\"))\n",
    "b = float(input(\"enter coeff of quadratic term\"))\n",
    "c = float(input(\"enter coeff of linear term\"))\n",
    "d = float(input(\"enter coeff of constant term\"))\n",
    "coeff = (a,b,c,d)\n",
    "x = float(input(\"what is the value of x?\"))\n",
    "def slope_of_cubic(coefficients, value):\n",
    "    slope = 3 * coefficients[0] * value ** 2 + 2 * coefficients[1] * value + coefficients[2]\n",
    "    print(\"the slope of the cubic polynomial is\", slope)\n",
    "slope_of_cubic(coeff, x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0b84114b-dc45-4ce3-822a-bb884a6f1b7f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
