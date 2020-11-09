{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Internship Project"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "The data is for company X which is trying to control attrition. There are two sets of data: \"Existing employees\" and \"Employees who have left\". Following attributes are available for every employee.\n",
    "-Satisfaction Level\n",
    "-Last evaluation\n",
    "-Number of projects\n",
    "-Average monthly hours\n",
    "-Time spent at the company\n",
    "-Whether they have had a work accident\n",
    "-Whether they have had a promotion in the last 5 years\n",
    "-Departments (column sales)\n",
    "-Salary\n",
    "-Whether the employee has left\n",
    "\n",
    "Objective\n",
    "\n",
    "What type of employees are leaving? Determine which employees are prone to leave next. Present your results in the presentation sheet's presentation area."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Import necessary Libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import preprocessing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_excel('Company_X.xlsx',sheet_name=0)"
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
       "      <th>satisfacti</th>\n",
       "      <th>last_eval</th>\n",
       "      <th>number_</th>\n",
       "      <th>average_</th>\n",
       "      <th>time_spe</th>\n",
       "      <th>Work_acc</th>\n",
       "      <th>promotio</th>\n",
       "      <th>dept</th>\n",
       "      <th>salary</th>\n",
       "      <th>Emp_leave</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.58</td>\n",
       "      <td>0.74</td>\n",
       "      <td>4</td>\n",
       "      <td>215</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>sales</td>\n",
       "      <td>low</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.82</td>\n",
       "      <td>0.67</td>\n",
       "      <td>2</td>\n",
       "      <td>202</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>sales</td>\n",
       "      <td>low</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.45</td>\n",
       "      <td>0.69</td>\n",
       "      <td>5</td>\n",
       "      <td>193</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>sales</td>\n",
       "      <td>low</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.78</td>\n",
       "      <td>0.82</td>\n",
       "      <td>5</td>\n",
       "      <td>247</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>sales</td>\n",
       "      <td>low</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.49</td>\n",
       "      <td>0.60</td>\n",
       "      <td>3</td>\n",
       "      <td>214</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>sales</td>\n",
       "      <td>low</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14994</th>\n",
       "      <td>0.40</td>\n",
       "      <td>0.57</td>\n",
       "      <td>2</td>\n",
       "      <td>151</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>support</td>\n",
       "      <td>low</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14995</th>\n",
       "      <td>0.37</td>\n",
       "      <td>0.48</td>\n",
       "      <td>2</td>\n",
       "      <td>160</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>support</td>\n",
       "      <td>low</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14996</th>\n",
       "      <td>0.37</td>\n",
       "      <td>0.53</td>\n",
       "      <td>2</td>\n",
       "      <td>143</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>support</td>\n",
       "      <td>low</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14997</th>\n",
       "      <td>0.11</td>\n",
       "      <td>0.96</td>\n",
       "      <td>6</td>\n",
       "      <td>280</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>support</td>\n",
       "      <td>low</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14998</th>\n",
       "      <td>0.37</td>\n",
       "      <td>0.52</td>\n",
       "      <td>2</td>\n",
       "      <td>158</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>support</td>\n",
       "      <td>low</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>14999 rows × 10 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       satisfacti  last_eval  number_  average_  time_spe  Work_acc  promotio  \\\n",
       "0            0.58       0.74        4       215         3         0         0   \n",
       "1            0.82       0.67        2       202         3         0         0   \n",
       "2            0.45       0.69        5       193         3         0         0   \n",
       "3            0.78       0.82        5       247         3         0         0   \n",
       "4            0.49       0.60        3       214         2         0         0   \n",
       "...           ...        ...      ...       ...       ...       ...       ...   \n",
       "14994        0.40       0.57        2       151         3         0         0   \n",
       "14995        0.37       0.48        2       160         3         0         0   \n",
       "14996        0.37       0.53        2       143         3         0         0   \n",
       "14997        0.11       0.96        6       280         4         0         0   \n",
       "14998        0.37       0.52        2       158         3         0         0   \n",
       "\n",
       "          dept salary  Emp_leave  \n",
       "0        sales    low          0  \n",
       "1        sales    low          0  \n",
       "2        sales    low          0  \n",
       "3        sales    low          0  \n",
       "4        sales    low          0  \n",
       "...        ...    ...        ...  \n",
       "14994  support    low          1  \n",
       "14995  support    low          1  \n",
       "14996  support    low          1  \n",
       "14997  support    low          1  \n",
       "14998  support    low          1  \n",
       "\n",
       "[14999 rows x 10 columns]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
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
       "<bound method DataFrame.info of        satisfacti  last_eval  number_  average_  time_spe  Work_acc  promotio  \\\n",
       "0            0.58       0.74        4       215         3         0         0   \n",
       "1            0.82       0.67        2       202         3         0         0   \n",
       "2            0.45       0.69        5       193         3         0         0   \n",
       "3            0.78       0.82        5       247         3         0         0   \n",
       "4            0.49       0.60        3       214         2         0         0   \n",
       "...           ...        ...      ...       ...       ...       ...       ...   \n",
       "14994        0.40       0.57        2       151         3         0         0   \n",
       "14995        0.37       0.48        2       160         3         0         0   \n",
       "14996        0.37       0.53        2       143         3         0         0   \n",
       "14997        0.11       0.96        6       280         4         0         0   \n",
       "14998        0.37       0.52        2       158         3         0         0   \n",
       "\n",
       "          dept salary  Emp_leave  \n",
       "0        sales    low          0  \n",
       "1        sales    low          0  \n",
       "2        sales    low          0  \n",
       "3        sales    low          0  \n",
       "4        sales    low          0  \n",
       "...        ...    ...        ...  \n",
       "14994  support    low          1  \n",
       "14995  support    low          1  \n",
       "14996  support    low          1  \n",
       "14997  support    low          1  \n",
       "14998  support    low          1  \n",
       "\n",
       "[14999 rows x 10 columns]>"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.info"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "### Data Cleaning"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "satisfacti    float64\n",
       "last_eval     float64\n",
       "number_         int64\n",
       "average_        int64\n",
       "time_spe        int64\n",
       "Work_acc        int64\n",
       "promotio        int64\n",
       "dept           object\n",
       "salary         object\n",
       "Emp_leave       int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<bound method DataFrame.dropna of        satisfacti  last_eval  number_  average_  time_spe  Work_acc  promotio  \\\n",
       "0            0.58       0.74        4       215         3         0         0   \n",
       "1            0.82       0.67        2       202         3         0         0   \n",
       "2            0.45       0.69        5       193         3         0         0   \n",
       "3            0.78       0.82        5       247         3         0         0   \n",
       "4            0.49       0.60        3       214         2         0         0   \n",
       "...           ...        ...      ...       ...       ...       ...       ...   \n",
       "14994        0.40       0.57        2       151         3         0         0   \n",
       "14995        0.37       0.48        2       160         3         0         0   \n",
       "14996        0.37       0.53        2       143         3         0         0   \n",
       "14997        0.11       0.96        6       280         4         0         0   \n",
       "14998        0.37       0.52        2       158         3         0         0   \n",
       "\n",
       "          dept salary  Emp_leave  \n",
       "0        sales    low          0  \n",
       "1        sales    low          0  \n",
       "2        sales    low          0  \n",
       "3        sales    low          0  \n",
       "4        sales    low          0  \n",
       "...        ...    ...        ...  \n",
       "14994  support    low          1  \n",
       "14995  support    low          1  \n",
       "14996  support    low          1  \n",
       "14997  support    low          1  \n",
       "14998  support    low          1  \n",
       "\n",
       "[14999 rows x 10 columns]>"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dropna"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(14999, 10)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Label encoder"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import label encoder \n",
    "from sklearn import preprocessing \n",
    "\n",
    "# label_encoder object knows how to understand word labels. \n",
    "le = preprocessing.LabelEncoder() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Encode labels in column 'dept'. \n",
    "df['dept']= le.fit_transform(df['dept']) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Encode labels in column 'Species'. \n",
    "df['salary']= le.fit_transform(df['salary']) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 0])"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['salary'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([7, 2, 3, 9, 8, 4, 0, 6, 1, 5])"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['dept'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "satisfacti    float64\n",
       "last_eval     float64\n",
       "number_         int64\n",
       "average_        int64\n",
       "time_spe        int64\n",
       "Work_acc        int64\n",
       "promotio        int64\n",
       "dept            int32\n",
       "salary          int32\n",
       "Emp_leave       int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"Labels =\", labels)\n",
    "print(\"Encoded labels =\", list(encoded_labels))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split # Import train_test_split function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.rename(columns = {\"number_\":\"no_of_proj\",\"average_\":\"av_mnth_hrs\",\"promotio\":\"promotion\",\"Emp_leave\":\"left\",\"satisfacti\":\"satisfaction\"},inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
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
       "      <th>satisfaction</th>\n",
       "      <th>last_eval</th>\n",
       "      <th>no_of_proj</th>\n",
       "      <th>av_mnth_hrs</th>\n",
       "      <th>time_spe</th>\n",
       "      <th>Work_acc</th>\n",
       "      <th>promotion</th>\n",
       "      <th>dept</th>\n",
       "      <th>salary</th>\n",
       "      <th>left</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.58</td>\n",
       "      <td>0.74</td>\n",
       "      <td>4</td>\n",
       "      <td>215</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.82</td>\n",
       "      <td>0.67</td>\n",
       "      <td>2</td>\n",
       "      <td>202</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.45</td>\n",
       "      <td>0.69</td>\n",
       "      <td>5</td>\n",
       "      <td>193</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.78</td>\n",
       "      <td>0.82</td>\n",
       "      <td>5</td>\n",
       "      <td>247</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.49</td>\n",
       "      <td>0.60</td>\n",
       "      <td>3</td>\n",
       "      <td>214</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14994</th>\n",
       "      <td>0.40</td>\n",
       "      <td>0.57</td>\n",
       "      <td>2</td>\n",
       "      <td>151</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>8</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14995</th>\n",
       "      <td>0.37</td>\n",
       "      <td>0.48</td>\n",
       "      <td>2</td>\n",
       "      <td>160</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>8</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14996</th>\n",
       "      <td>0.37</td>\n",
       "      <td>0.53</td>\n",
       "      <td>2</td>\n",
       "      <td>143</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>8</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14997</th>\n",
       "      <td>0.11</td>\n",
       "      <td>0.96</td>\n",
       "      <td>6</td>\n",
       "      <td>280</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>8</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14998</th>\n",
       "      <td>0.37</td>\n",
       "      <td>0.52</td>\n",
       "      <td>2</td>\n",
       "      <td>158</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>8</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>14999 rows × 10 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       satisfaction  last_eval  no_of_proj  av_mnth_hrs  time_spe  Work_acc  \\\n",
       "0              0.58       0.74           4          215         3         0   \n",
       "1              0.82       0.67           2          202         3         0   \n",
       "2              0.45       0.69           5          193         3         0   \n",
       "3              0.78       0.82           5          247         3         0   \n",
       "4              0.49       0.60           3          214         2         0   \n",
       "...             ...        ...         ...          ...       ...       ...   \n",
       "14994          0.40       0.57           2          151         3         0   \n",
       "14995          0.37       0.48           2          160         3         0   \n",
       "14996          0.37       0.53           2          143         3         0   \n",
       "14997          0.11       0.96           6          280         4         0   \n",
       "14998          0.37       0.52           2          158         3         0   \n",
       "\n",
       "       promotion  dept  salary  left  \n",
       "0              0     7       1     0  \n",
       "1              0     7       1     0  \n",
       "2              0     7       1     0  \n",
       "3              0     7       1     0  \n",
       "4              0     7       1     0  \n",
       "...          ...   ...     ...   ...  \n",
       "14994          0     8       1     1  \n",
       "14995          0     8       1     1  \n",
       "14996          0     8       1     1  \n",
       "14997          0     8       1     1  \n",
       "14998          0     8       1     1  \n",
       "\n",
       "[14999 rows x 10 columns]"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.groupby('left').mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "#split dataset in features and target variable\n",
    "feature_cols = ['last_eval','no_of_proj','av_mnth_hrs','Work_acc','satisfaction','promotion', 'dept','salary','left']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "feature_cols = ['dept','salary','left']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = df[feature_cols] # Features\n",
    "y = df.left # Target variable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Split dataset into training set and test set\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create Decision Tree classifer object\n",
    "clf = DecisionTreeClassifier()\n",
    "\n",
    "# Train Decision Tree Classifer\n",
    "clf = clf.fit(X_train,y_train)\n",
    "\n",
    "#Predict the response for test dataset\n",
    "y_pred = clf.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 1.0\n"
     ]
    }
   ],
   "source": [
    "print(\"Accuracy:\",metrics.accuracy_score(y_test, y_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn import datasets\n",
    "from sklearn import svm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((12749, 9), (12749,))"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train.shape, y_train.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((2250, 9), (2250,))"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test.shape, y_test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.score(X_test, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\User\\anaconda3\\lib\\site-packages\\pandas\\core\\ops\\array_ops.py:253: FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison\n",
      "  res_values = method(rvalues)\n"
     ]
    }
   ],
   "source": [
    "df['dept']=np.where(df['dept'] =='support', 'technical', df['dept'])\n",
    "df['dept']=np.where(df['dept'] =='IT', 'technical', df['dept'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['7', '2', '3', '9', '8', '4', '0', '6', '1', '5'], dtype=object)"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['dept'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import the class\n",
    "from sklearn.linear_model import LogisticRegression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "#split dataset in features and target variable\n",
    "feature_cols = ['promotion', 'dept','salary','left']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "X1 = df[feature_cols] # Features\n",
    "y1= df.left # Target variable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "X1_train,X1_test,y1_train,y1_test=train_test_split(X1,y1,test_size=0.30,random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "# instantiate the model (using the default parameters)\n",
    "logreg = LogisticRegression()\n",
    "\n",
    "# fit the model with data\n",
    "logreg.fit(X1_train,y1_train)\n",
    "\n",
    "#\n",
    "y1_pred=logreg.predict(X1_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 1.0\n"
     ]
    }
   ],
   "source": [
    "print(\"Accuracy:\",metrics.accuracy_score(y1_test, y1_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3429,    0],\n",
       "       [   0, 1071]], dtype=int64)"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# import the metrics class\n",
    "from sklearn import metrics\n",
    "cnf_matrix = metrics.confusion_matrix(y1_test, y1_pred)\n",
    "cnf_matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import required modules\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 257.44, 'Predicted label')"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "class_names=[0,1] # name  of classes\n",
    "fig, ax = plt.subplots()\n",
    "tick_marks = np.arange(len(class_names))\n",
    "plt.xticks(tick_marks, class_names)\n",
    "plt.yticks(tick_marks, class_names)\n",
    "# create heatmap\n",
    "sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap=\"YlGnBu\" ,fmt='g')\n",
    "ax.xaxis.set_label_position(\"top\")\n",
    "plt.tight_layout()\n",
    "plt.title('Confusion matrix', y=1.1)\n",
    "plt.ylabel('Actual label')\n",
    "plt.xlabel('Predicted label')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 1.0\n",
      "Precision: 1.0\n",
      "Recall: 1.0\n"
     ]
    }
   ],
   "source": [
    "print(\"Accuracy:\",metrics.accuracy_score(y_test, y_pred))\n",
    "print(\"Precision:\",metrics.precision_score(y_test, y_pred))\n",
    "print(\"Recall:\",metrics.recall_score(y_test, y_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXQAAAD4CAYAAAD8Zh1EAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjMsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+AADFEAAASxElEQVR4nO3dfYxddZ3H8fdXBmjMFit0SIApTldqbEEeR5AaFYIPpQmtT5ESXWFT2wW2bFJlAxuJ1oIJAluyJF2hCkGIWBEVCtY0QYoaI2ynacE+yDpQkKG6TMtTCa1t5bt/zGUyTGd6z7R3Zjq/vl/JJPec851zvr/emc+c/s6990RmIkka/d4x0g1IkhrDQJekQhjoklQIA12SCmGgS1IhmkbqwOPHj8/W1taROrwkjUqrV6/ekpnN/W0bsUBvbW2lvb19pA4vSaNSRDw30DanXCSpEAa6JBXCQJekQhjoklQIA12SClE30CPijoh4MSLWDbA9IuKWiOiIiCcj4vTGtylJqqfKGfqdwLS9bD8fmFT7mgt8d//bkiQNVt3XoWfmbyKidS8lM4G7svtzeB+LiHERcUxm/qVBPb7NPY//mQfWvjAUu5akYTHl2CP45gUnNny/jZhDPw54vtdyZ23dHiJibkS0R0R7V1fXPh3sgbUv8Piml/bpeyWpZI14p2j0s67fu2Zk5hJgCUBbW9s+31njrIlH8uN/OXtfv12SitSIM/ROYEKv5RZgcwP2K0kahEYE+jLgy7VXu3wIeHWo5s8lSQOrO+USET8CzgHGR0Qn8E3gUIDMvBVYDkwHOoA3gH8eqmYlSQOr8iqXi+psT+BfG9aRJGmf+E5RSSqEgS5JhTDQJakQBrokFcJAl6RCGOiSVAgDXZIKYaBLUiEMdEkqhIEuSYUw0CWpEAa6JBXCQJekQhjoklQIA12SCmGgS1IhDHRJKoSBLkmFMNAlqRAGuiQVwkCXpEIY6JJUCANdkgphoEtSIQx0SSqEgS5JhTDQJakQBrokFcJAl6RCGOiSVAgDXZIKUSnQI2JaRDwVER0RcXU/24+PiJURsSYinoyI6Y1vVZK0N3UDPSIOARYD5wNTgIsiYkqfsmuAezPzNGAW8N+NblSStHdVztDPBDoy85nM3AksBWb2qUngiNrjdwGbG9eiJKmKKoF+HPB8r+XO2rreFgBfiohOYDlwRX87ioi5EdEeEe1dXV370K4kaSBVAj36WZd9li8C7szMFmA6cHdE7LHvzFySmW2Z2dbc3Dz4biVJA6oS6J3AhF7LLew5pTIbuBcgM38PjAHGN6JBSVI1VQJ9FTApIiZGxGF0X/Rc1qfmz8B5ABExme5Ad05FkoZR3UDPzN3APGAFsJHuV7Osj4iFETGjVvY1YE5EPAH8CLgkM/tOy0iShlBTlaLMXE73xc7e677R6/EG4MONbU2SNBi+U1SSCmGgS1IhDHRJKoSBLkmFMNAlqRAGuiQVwkCXpEIY6JJUCANdkgphoEtSIQx0SSqEgS5JhTDQJakQBrokFcJAl6RCGOiSVAgDXZIKYaBLUiEMdEkqhIEuSYUw0CWpEAa6JBXCQJekQhjoklQIA12SCmGgS1IhDHRJKoSBLkmFMNAlqRAGuiQVolKgR8S0iHgqIjoi4uoBar4QERsiYn1E3NPYNiVJ9TTVK4iIQ4DFwCeATmBVRCzLzA29aiYB/wF8ODNfjoijh6phSVL/qpyhnwl0ZOYzmbkTWArM7FMzB1icmS8DZOaLjW1TklRPlUA/Dni+13JnbV1v7wPeFxG/i4jHImJafzuKiLkR0R4R7V1dXfvWsSSpX1UCPfpZl32Wm4BJwDnARcD3I2LcHt+UuSQz2zKzrbm5ebC9SpL2okqgdwITei23AJv7qXkgM3dl5ibgKboDXpI0TKoE+ipgUkRMjIjDgFnAsj419wPnAkTEeLqnYJ5pZKOSpL2rG+iZuRuYB6wANgL3Zub6iFgYETNqZSuArRGxAVgJ/Htmbh2qpiVJe6r7skWAzFwOLO+z7hu9Hifw1dqXJGkE+E5RSSqEgS5JhTDQJakQBrokFcJAl6RCGOiSVAgDXZIKYaBLUiEMdEkqhIEuSYUw0CWpEAa6JBXCQJekQhjoklQIA12SCmGgS1IhDHRJKoSBLkmFMNAlqRAGuiQVwkCXpEIY6JJUCANdkgphoEtSIQx0SSqEgS5JhTDQJakQBrokFcJAl6RCGOiSVAgDXZIKUSnQI2JaRDwVER0RcfVe6j4fERkRbY1rUZJURd1Aj4hDgMXA+cAU4KKImNJP3Vjg34DHG92kJKm+KmfoZwIdmflMZu4ElgIz+6m7FrgB2NHA/iRJFVUJ9OOA53std9bW9YiI04AJmfnQ3nYUEXMjoj0i2ru6ugbdrCRpYFUCPfpZlz0bI94B3Ax8rd6OMnNJZrZlZltzc3P1LiVJdVUJ9E5gQq/lFmBzr+WxwEnAoxHxLPAhYJkXRiVpeFUJ9FXApIiYGBGHAbOAZW9tzMxXM3N8ZrZmZivwGDAjM9uHpGNJUr/qBnpm7gbmASuAjcC9mbk+IhZGxIyhblCSVE1TlaLMXA4s77PuGwPUnrP/bUmSBst3ikpSIQx0SSqEgS5JhTDQJakQBrokFcJAl6RCGOiSVAgDXZIKYaBLUiEMdEkqhIEuSYUw0CWpEAa6JBXCQJekQhjoklQIA12SCmGgS1IhDHRJKoSBLkmFMNAlqRAGuiQVwkCXpEIY6JJUCANdkgphoEtSIQx0SSqEgS5JhTDQJakQBrokFcJAl6RCVAr0iJgWEU9FREdEXN3P9q9GxIaIeDIifhUR72l8q5Kkvakb6BFxCLAYOB+YAlwUEVP6lK0B2jLzZOA+4IZGNypJ2rsqZ+hnAh2Z+Uxm7gSWAjN7F2Tmysx8o7b4GNDS2DYlSfVUCfTjgOd7LXfW1g1kNvDL/jZExNyIaI+I9q6urupdSpLqqhLo0c+67Lcw4ktAG3Bjf9szc0lmtmVmW3Nzc/UuJUl1NVWo6QQm9FpuATb3LYqIjwNfBz6WmX9rTHuSpKqqnKGvAiZFxMSIOAyYBSzrXRARpwG3ATMy88XGtylJqqduoGfmbmAesALYCNybmesjYmFEzKiV3Qj8A/CTiFgbEcsG2J0kaYhUmXIhM5cDy/us+0avxx9vcF+SpEHynaKSVAgDXZIKYaBLUiEMdEkqhIEuSYUw0CWpEAa6JBXCQJekQhjoklQIA12SCmGgS1IhDHRJKoSBLkmFMNAlqRAGuiQVwkCXpEIY6JJUCANdkgphoEtSIQx0SSqEgS5JhWga6QYkNcauXbvo7Oxkx44dI92KGmDMmDG0tLRw6KGHVv4eA10qRGdnJ2PHjqW1tZWIGOl2tB8yk61bt9LZ2cnEiRMrf59TLlIhduzYwVFHHWWYFyAiOOqoowb9vy0DXSqIYV6OfXkuDXRJKoSBLmlILFiwgJtuummvNffffz8bNmwY1H7/+Mc/cvbZZ3P44YfX3f9wq9rbpk2bOOuss5g0aRIXXnghO3fubMjxDXRJI2ZfAv3II4/klltu4corrxyirvZd1d6uuuoq5s+fz5/+9Cfe/e53c/vttzfk+L7KRSrQtx5cz4bNrzV0n1OOPYJvXnDiXmu+/e1vc9dddzFhwgSam5s544wzAPje977HkiVL2LlzJyeccAJ33303a9euZdmyZfz617/muuuu46c//SmPPPLIHnXvfOc733aMo48+mqOPPppf/OIXlXtfuHAhDz74INu3b2fq1KncdtttRATnnHMON910E21tbWzZsoW2tjaeffZZ/v73v3PVVVexYsUKIoI5c+ZwxRVX1D1Old4yk0ceeYR77rkHgIsvvpgFCxZw2WWXVR7PQDxDl9QQq1evZunSpaxZs4af/exnrFq1qmfbZz/7WVatWsUTTzzB5MmTuf3225k6dSozZszgxhtvZO3atbz3ve/tt64R5s2bx6pVq1i3bh3bt2/noYce2mv9kiVL2LRpE2vWrOHJJ5/ki1/8IgDz58/n1FNP3ePr+uuvr9zL1q1bGTduHE1N3efTLS0tvPDCC/s+uF48Q5cKVO9Meij89re/5TOf+UzPGfWMGTN6tq1bt45rrrmGV155hddff51PfepT/e6jat1grVy5khtuuIE33niDl156iRNPPJELLrhgwPqHH36YSy+9tCd0jzzySABuvvnm/e4lM/dY16hXJ1UK9IiYBvwXcAjw/cy8vs/2w4G7gDOArcCFmflsQzqUNGoMFEyXXHIJ999/P6eccgp33nknjz766H7VDcaOHTu4/PLLaW9vZ8KECSxYsKDn9d1NTU28+eabPXVvycx+xzJ//nxWrly5x/pZs2Zx9dVXV+pn/PjxvPLKK+zevZumpiY6Ozs59thj92Voe6g75RIRhwCLgfOBKcBFETGlT9ls4OXMPAG4GfhOQ7qTNGp89KMf5ec//znbt29n27ZtPPjggz3btm3bxjHHHMOuXbv44Q9/2LN+7NixbNu2rW5dVeedd94e0xdvBfX48eN5/fXXue+++3q2tba2snr1aoC3rf/kJz/Jrbfeyu7duwF46aWXgO4z9LVr1+7xVTXMofuP3rnnnttzvB/84AfMnDlz0GPtT5U59DOBjsx8JjN3AkuBvkefCfyg9vg+4LzwHQ7SQeX000/nwgsv5NRTT+Vzn/scH/nIR3q2XXvttZx11ll84hOf4P3vf3/P+lmzZnHjjTdy2mmn8fTTTw9Y19tf//pXWlpaWLRoEddddx0tLS289tprvPnmm3R0dPRMj7xl3LhxzJkzhw984AN8+tOf5oMf/GDPtiuvvJLvfve7TJ06lS1btvSs/8pXvsLxxx/PySefzCmnnNJzAbOegXoDmD59Ops3bwbgO9/5DosWLeKEE05g69atzJ49u9L+64n+5nPeVhDxeWBaZn6ltvxPwFmZOa9XzbpaTWdt+elazZY++5oLzAU4/vjjz3juuecG3fC3HlwPjMwcoXQg27hxI5MnTx7pNkbMunXruOOOO1i0aNFIt9Iw/T2nEbE6M9v6q68yh97fmXbfvwJVasjMJcASgLa2tr3/JRmAQS6pPyeddFJRYb4vqky5dAITei23AJsHqomIJuBdwEuNaFCSVE2VQF8FTIqIiRFxGDALWNanZhlwce3x54FHst5cjqSG89euHPvyXNYN9MzcDcwDVgAbgXszc31ELIyIt15oejtwVER0AF8Fql/yldQQY8aMYevWrYZ6Ad76PPQxY8YM6vvqXhQdKm1tbdne3j4ix5ZK5B2LyjLQHYv296KopFHg0EMPHdTdbVQeP8tFkgphoEtSIQx0SSrEiF0UjYguYPBvFe02HthSt6osjvng4JgPDvsz5vdkZnN/G0Ys0PdHRLQPdJW3VI754OCYDw5DNWanXCSpEAa6JBVitAb6kpFuYAQ45oODYz44DMmYR+UcuiRpT6P1DF2S1IeBLkmFOKADPSKmRcRTEdEREXt8gmNEHB4RP65tfzwiWoe/y8aqMOavRsSGiHgyIn4VEe8ZiT4bqd6Ye9V9PiIyIkb9S9yqjDkivlB7rtdHRLV7oB3AKvxsHx8RKyNiTe3ne/pI9NkoEXFHRLxYu6Nbf9sjIm6p/Xs8GRGn7/dBM/OA/AIOAZ4G/hE4DHgCmNKn5nLg1trjWcCPR7rvYRjzucA7a48vOxjGXKsbC/wGeAxoG+m+h+F5ngSsAd5dWz56pPsehjEvAS6rPZ4CPDvSfe/nmD8KnA6sG2D7dOCXdN/x7UPA4/t7zAP5DP1gvDl13TFn5srMfKO2+Bjdd5Aazao8zwDXAjcAJXw2bJUxzwEWZ+bLAJn54jD32GhVxpzAEbXH72LPO6ONKpn5G/Z+57aZwF3Z7TFgXEQcsz/HPJAD/Tjg+V7LnbV1/dZk9404XgWOGpbuhkaVMfc2m+6/8KNZ3TFHxGnAhMx8aDgbG0JVnuf3Ae+LiN9FxGMRMW3YuhsaVca8APhSRHQCy4Erhqe1ETPY3/e6DuTPQ2/YzalHkcrjiYgvAW3Ax4a0o6G31zFHxDuAm4FLhquhYVDleW6ie9rlHLr/F/bbiDgpM18Z4t6GSpUxXwTcmZn/GRFnA3fXxvzm0Lc3IhqeXwfyGfrBeHPqKmMmIj4OfB2YkZl/G6behkq9MY8FTgIejYhn6Z5rXDbKL4xW/dl+IDN3ZeYm4Cm6A360qjLm2cC9AJn5e2AM3R9iVapKv++DcSAH+sF4c+q6Y65NP9xGd5iP9nlVqDPmzHw1M8dnZmtmttJ93WBGZo7m+xdW+dm+n+4L4ETEeLqnYJ4Z1i4bq8qY/wycBxARk+kO9K5h7XJ4LQO+XHu1y4eAVzPzL/u1x5G+ElznKvF04H/pvjr+9dq6hXT/QkP3E/4ToAP4H+AfR7rnYRjzw8D/AWtrX8tGuuehHnOf2kcZ5a9yqfg8B7AI2AD8AZg10j0Pw5inAL+j+xUwa4FPjnTP+zneHwF/AXbRfTY+G7gUuLTXc7y49u/xh0b8XPvWf0kqxIE85SJJGgQDXZIKYaBLUiEMdEkqhIEuSYUw0CWpEAa6JBXi/wE0v+GRMYq4+wAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "y1_pred_proba = logreg.predict_proba(X1_test)[::,1]\n",
    "fpr, tpr, _ = metrics.roc_curve(y1_test,  y1_pred_proba)\n",
    "auc = metrics.roc_auc_score(y1_test, y1_pred_proba)\n",
    "plt.plot(fpr,tpr,label=\"data 1, auc=\"+str(auc))\n",
    "plt.legend(loc=4)\n",
    "plt.show()"
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
