{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Assignment 2 : Titanic Data Predictions\n",
    "### Importing Required Libraries and Loading Data\n",
    "#### Importing Libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Loading Dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>pclass</th>\n",
       "      <th>survived</th>\n",
       "      <th>name</th>\n",
       "      <th>sex</th>\n",
       "      <th>age</th>\n",
       "      <th>sibsp</th>\n",
       "      <th>parch</th>\n",
       "      <th>ticket</th>\n",
       "      <th>fare</th>\n",
       "      <th>cabin</th>\n",
       "      <th>embarked</th>\n",
       "      <th>boat</th>\n",
       "      <th>body</th>\n",
       "      <th>home.dest</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Allen, Miss. Elisabeth Walton</td>\n",
       "      <td>female</td>\n",
       "      <td>29.00</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>24160</td>\n",
       "      <td>211.3375</td>\n",
       "      <td>B5</td>\n",
       "      <td>S</td>\n",
       "      <td>2</td>\n",
       "      <td>NaN</td>\n",
       "      <td>St Louis, MO</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Allison, Master. Hudson Trevor</td>\n",
       "      <td>male</td>\n",
       "      <td>0.92</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>113781</td>\n",
       "      <td>151.5500</td>\n",
       "      <td>C22 C26</td>\n",
       "      <td>S</td>\n",
       "      <td>11</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Montreal, PQ / Chesterville, ON</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Allison, Miss. Helen Loraine</td>\n",
       "      <td>female</td>\n",
       "      <td>2.00</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>113781</td>\n",
       "      <td>151.5500</td>\n",
       "      <td>C22 C26</td>\n",
       "      <td>S</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Montreal, PQ / Chesterville, ON</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Allison, Mr. Hudson Joshua Creighton</td>\n",
       "      <td>male</td>\n",
       "      <td>30.00</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>113781</td>\n",
       "      <td>151.5500</td>\n",
       "      <td>C22 C26</td>\n",
       "      <td>S</td>\n",
       "      <td>NaN</td>\n",
       "      <td>135.0</td>\n",
       "      <td>Montreal, PQ / Chesterville, ON</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Allison, Mrs. Hudson J C (Bessie Waldo Daniels)</td>\n",
       "      <td>female</td>\n",
       "      <td>25.00</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>113781</td>\n",
       "      <td>151.5500</td>\n",
       "      <td>C22 C26</td>\n",
       "      <td>S</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Montreal, PQ / Chesterville, ON</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   pclass  survived                                             name     sex  \\\n",
       "0       1         1                    Allen, Miss. Elisabeth Walton  female   \n",
       "1       1         1                   Allison, Master. Hudson Trevor    male   \n",
       "2       1         0                     Allison, Miss. Helen Loraine  female   \n",
       "3       1         0             Allison, Mr. Hudson Joshua Creighton    male   \n",
       "4       1         0  Allison, Mrs. Hudson J C (Bessie Waldo Daniels)  female   \n",
       "\n",
       "     age  sibsp  parch  ticket      fare    cabin embarked boat   body  \\\n",
       "0  29.00      0      0   24160  211.3375       B5        S    2    NaN   \n",
       "1   0.92      1      2  113781  151.5500  C22 C26        S   11    NaN   \n",
       "2   2.00      1      2  113781  151.5500  C22 C26        S  NaN    NaN   \n",
       "3  30.00      1      2  113781  151.5500  C22 C26        S  NaN  135.0   \n",
       "4  25.00      1      2  113781  151.5500  C22 C26        S  NaN    NaN   \n",
       "\n",
       "                         home.dest  \n",
       "0                     St Louis, MO  \n",
       "1  Montreal, PQ / Chesterville, ON  \n",
       "2  Montreal, PQ / Chesterville, ON  \n",
       "3  Montreal, PQ / Chesterville, ON  \n",
       "4  Montreal, PQ / Chesterville, ON  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "url = \"https://biostat.app.vumc.org/wiki/pub/Main/DataSets/titanic3.csv\"\n",
    "df = pd.read_csv(url)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Preprocessing the Data\n",
    "### Display Some basic Information of the Dataset\n",
    "#### Describe the Datatset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>pclass</th>\n",
       "      <th>survived</th>\n",
       "      <th>age</th>\n",
       "      <th>sibsp</th>\n",
       "      <th>parch</th>\n",
       "      <th>fare</th>\n",
       "      <th>body</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1309.000000</td>\n",
       "      <td>1309.000000</td>\n",
       "      <td>1046.000000</td>\n",
       "      <td>1309.000000</td>\n",
       "      <td>1309.000000</td>\n",
       "      <td>1308.000000</td>\n",
       "      <td>121.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>2.294882</td>\n",
       "      <td>0.381971</td>\n",
       "      <td>29.881138</td>\n",
       "      <td>0.498854</td>\n",
       "      <td>0.385027</td>\n",
       "      <td>33.295479</td>\n",
       "      <td>160.809917</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.837836</td>\n",
       "      <td>0.486055</td>\n",
       "      <td>14.413493</td>\n",
       "      <td>1.041658</td>\n",
       "      <td>0.865560</td>\n",
       "      <td>51.758668</td>\n",
       "      <td>97.696922</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.170000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>21.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>7.895800</td>\n",
       "      <td>72.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>28.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>14.454200</td>\n",
       "      <td>155.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>39.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>31.275000</td>\n",
       "      <td>256.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>512.329200</td>\n",
       "      <td>328.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            pclass     survived          age        sibsp        parch  \\\n",
       "count  1309.000000  1309.000000  1046.000000  1309.000000  1309.000000   \n",
       "mean      2.294882     0.381971    29.881138     0.498854     0.385027   \n",
       "std       0.837836     0.486055    14.413493     1.041658     0.865560   \n",
       "min       1.000000     0.000000     0.170000     0.000000     0.000000   \n",
       "25%       2.000000     0.000000    21.000000     0.000000     0.000000   \n",
       "50%       3.000000     0.000000    28.000000     0.000000     0.000000   \n",
       "75%       3.000000     1.000000    39.000000     1.000000     0.000000   \n",
       "max       3.000000     1.000000    80.000000     8.000000     9.000000   \n",
       "\n",
       "              fare        body  \n",
       "count  1308.000000  121.000000  \n",
       "mean     33.295479  160.809917  \n",
       "std      51.758668   97.696922  \n",
       "min       0.000000    1.000000  \n",
       "25%       7.895800   72.000000  \n",
       "50%      14.454200  155.000000  \n",
       "75%      31.275000  256.000000  \n",
       "max     512.329200  328.000000  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Display column names"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pclass         int64\n",
       "survived       int64\n",
       "name          object\n",
       "sex           object\n",
       "age          float64\n",
       "sibsp          int64\n",
       "parch          int64\n",
       "ticket        object\n",
       "fare         float64\n",
       "cabin         object\n",
       "embarked      object\n",
       "boat          object\n",
       "body         float64\n",
       "home.dest     object\n",
       "dtype: object"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Find Number of missing values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pclass - 0\n",
      "survived - 0\n",
      "name - 0\n",
      "sex - 0\n",
      "age - 263\n",
      "sibsp - 0\n",
      "parch - 0\n",
      "ticket - 0\n",
      "fare - 1\n",
      "cabin - 1014\n",
      "embarked - 2\n",
      "boat - 823\n",
      "body - 1188\n",
      "home.dest - 564\n"
     ]
    }
   ],
   "source": [
    "column_names = df.columns\n",
    "for column in column_names:\n",
    "    print(column + \" - \" + str(df[column].isnull().sum()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}