{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "#50\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
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
       "      <th>ID</th>\n",
       "      <th>TITLE</th>\n",
       "      <th>URL</th>\n",
       "      <th>PUBLISHER</th>\n",
       "      <th>CATEGORY</th>\n",
       "      <th>STORY</th>\n",
       "      <th>HOSTNAME</th>\n",
       "      <th>TIMESTAMP</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Fed official says weak data caused by weather,...</td>\n",
       "      <td>http://www.latimes.com/business/money/la-fi-mo...</td>\n",
       "      <td>Los Angeles Times</td>\n",
       "      <td>b</td>\n",
       "      <td>ddUyU0VZz0BRneMioxUPQVP6sIxvM</td>\n",
       "      <td>www.latimes.com</td>\n",
       "      <td>1394470370698</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Fed's Charles Plosser sees high bar for change...</td>\n",
       "      <td>http://www.livemint.com/Politics/H2EvwJSK2VE6O...</td>\n",
       "      <td>Livemint</td>\n",
       "      <td>b</td>\n",
       "      <td>ddUyU0VZz0BRneMioxUPQVP6sIxvM</td>\n",
       "      <td>www.livemint.com</td>\n",
       "      <td>1394470371207</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>US open: Stocks fall after Fed official hints ...</td>\n",
       "      <td>http://www.ifamagazine.com/news/us-open-stocks...</td>\n",
       "      <td>IFA Magazine</td>\n",
       "      <td>b</td>\n",
       "      <td>ddUyU0VZz0BRneMioxUPQVP6sIxvM</td>\n",
       "      <td>www.ifamagazine.com</td>\n",
       "      <td>1394470371550</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Fed risks falling 'behind the curve', Charles ...</td>\n",
       "      <td>http://www.ifamagazine.com/news/fed-risks-fall...</td>\n",
       "      <td>IFA Magazine</td>\n",
       "      <td>b</td>\n",
       "      <td>ddUyU0VZz0BRneMioxUPQVP6sIxvM</td>\n",
       "      <td>www.ifamagazine.com</td>\n",
       "      <td>1394470371793</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Fed's Plosser: Nasty Weather Has Curbed Job Gr...</td>\n",
       "      <td>http://www.moneynews.com/Economy/federal-reser...</td>\n",
       "      <td>Moneynews</td>\n",
       "      <td>b</td>\n",
       "      <td>ddUyU0VZz0BRneMioxUPQVP6sIxvM</td>\n",
       "      <td>www.moneynews.com</td>\n",
       "      <td>1394470372027</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    ID                                              TITLE  \\\n",
       "0    1  Fed official says weak data caused by weather,...   \n",
       "1    2  Fed's Charles Plosser sees high bar for change...   \n",
       "2    3  US open: Stocks fall after Fed official hints ...   \n",
       "3    4  Fed risks falling 'behind the curve', Charles ...   \n",
       "4    5  Fed's Plosser: Nasty Weather Has Curbed Job Gr...   \n",
       "\n",
       "                                                 URL          PUBLISHER  \\\n",
       "0  http://www.latimes.com/business/money/la-fi-mo...  Los Angeles Times   \n",
       "1  http://www.livemint.com/Politics/H2EvwJSK2VE6O...           Livemint   \n",
       "2  http://www.ifamagazine.com/news/us-open-stocks...       IFA Magazine   \n",
       "3  http://www.ifamagazine.com/news/fed-risks-fall...       IFA Magazine   \n",
       "4  http://www.moneynews.com/Economy/federal-reser...          Moneynews   \n",
       "\n",
       "  CATEGORY                          STORY             HOSTNAME      TIMESTAMP  \n",
       "0        b  ddUyU0VZz0BRneMioxUPQVP6sIxvM      www.latimes.com  1394470370698  \n",
       "1        b  ddUyU0VZz0BRneMioxUPQVP6sIxvM     www.livemint.com  1394470371207  \n",
       "2        b  ddUyU0VZz0BRneMioxUPQVP6sIxvM  www.ifamagazine.com  1394470371550  \n",
       "3        b  ddUyU0VZz0BRneMioxUPQVP6sIxvM  www.ifamagazine.com  1394470371793  \n",
       "4        b  ddUyU0VZz0BRneMioxUPQVP6sIxvM    www.moneynews.com  1394470372027  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "with open(\"NewsAggregatorDataset/newsCorpora.csv\", \"r\") as f:\n",
    "    df = pd.read_csv(f, sep=\"\\t\", header=None, names=[\" ID\", \"TITLE\", \"URL\", \"PUBLISHER\", \"CATEGORY\", \"STORY\" ,\"HOSTNAME\", \"TIMESTAMP\"])\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "extract_df = df[df[\"PUBLISHER\"].isin([\"Reuters\", \"Huffington Post\", \"Businessweek\", \"Contactmusic.com\", \"Daily Mail\"])]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
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
    "publisher_var = extract_df[\"PUBLISHER\"].value_counts() #PUBLISHERは既に抽出されている\n",
    "publisher_var.plot.bar()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
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
       "      <th>ID</th>\n",
       "      <th>TITLE</th>\n",
       "      <th>URL</th>\n",
       "      <th>PUBLISHER</th>\n",
       "      <th>CATEGORY</th>\n",
       "      <th>STORY</th>\n",
       "      <th>HOSTNAME</th>\n",
       "      <th>TIMESTAMP</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>13</td>\n",
       "      <td>Europe reaches crunch point on banking union</td>\n",
       "      <td>http://in.reuters.com/article/2014/03/10/eu-ba...</td>\n",
       "      <td>Reuters</td>\n",
       "      <td>b</td>\n",
       "      <td>dPhGU51DcrolUIMxbRm0InaHGA2XM</td>\n",
       "      <td>in.reuters.com</td>\n",
       "      <td>1394470501755</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>14</td>\n",
       "      <td>ECB FOCUS-Stronger euro drowns out ECB's messa...</td>\n",
       "      <td>http://in.reuters.com/article/2014/03/10/ecb-p...</td>\n",
       "      <td>Reuters</td>\n",
       "      <td>b</td>\n",
       "      <td>dPhGU51DcrolUIMxbRm0InaHGA2XM</td>\n",
       "      <td>in.reuters.com</td>\n",
       "      <td>1394470501948</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>20</td>\n",
       "      <td>Euro Anxieties Wane as Bunds Top Treasuries, S...</td>\n",
       "      <td>http://www.businessweek.com/news/2014-03-10/ge...</td>\n",
       "      <td>Businessweek</td>\n",
       "      <td>b</td>\n",
       "      <td>dPhGU51DcrolUIMxbRm0InaHGA2XM</td>\n",
       "      <td>www.businessweek.com</td>\n",
       "      <td>1394470503148</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>21</td>\n",
       "      <td>Noyer Says Strong Euro Creates Unwarranted Eco...</td>\n",
       "      <td>http://www.businessweek.com/news/2014-03-10/no...</td>\n",
       "      <td>Businessweek</td>\n",
       "      <td>b</td>\n",
       "      <td>dPhGU51DcrolUIMxbRm0InaHGA2XM</td>\n",
       "      <td>www.businessweek.com</td>\n",
       "      <td>1394470503366</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>30</td>\n",
       "      <td>REFILE-Bad loan triggers key feature in ECB ba...</td>\n",
       "      <td>http://in.reuters.com/article/2014/03/10/euroz...</td>\n",
       "      <td>Reuters</td>\n",
       "      <td>b</td>\n",
       "      <td>dPhGU51DcrolUIMxbRm0InaHGA2XM</td>\n",
       "      <td>in.reuters.com</td>\n",
       "      <td>1394470505070</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     ID                                              TITLE  \\\n",
       "12   13       Europe reaches crunch point on banking union   \n",
       "13   14  ECB FOCUS-Stronger euro drowns out ECB's messa...   \n",
       "19   20  Euro Anxieties Wane as Bunds Top Treasuries, S...   \n",
       "20   21  Noyer Says Strong Euro Creates Unwarranted Eco...   \n",
       "29   30  REFILE-Bad loan triggers key feature in ECB ba...   \n",
       "\n",
       "                                                  URL     PUBLISHER CATEGORY  \\\n",
       "12  http://in.reuters.com/article/2014/03/10/eu-ba...       Reuters        b   \n",
       "13  http://in.reuters.com/article/2014/03/10/ecb-p...       Reuters        b   \n",
       "19  http://www.businessweek.com/news/2014-03-10/ge...  Businessweek        b   \n",
       "20  http://www.businessweek.com/news/2014-03-10/no...  Businessweek        b   \n",
       "29  http://in.reuters.com/article/2014/03/10/euroz...       Reuters        b   \n",
       "\n",
       "                            STORY              HOSTNAME      TIMESTAMP  \n",
       "12  dPhGU51DcrolUIMxbRm0InaHGA2XM        in.reuters.com  1394470501755  \n",
       "13  dPhGU51DcrolUIMxbRm0InaHGA2XM        in.reuters.com  1394470501948  \n",
       "19  dPhGU51DcrolUIMxbRm0InaHGA2XM  www.businessweek.com  1394470503148  \n",
       "20  dPhGU51DcrolUIMxbRm0InaHGA2XM  www.businessweek.com  1394470503366  \n",
       "29  dPhGU51DcrolUIMxbRm0InaHGA2XM        in.reuters.com  1394470505070  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "extract_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "extract_df = extract_df[[\"CATEGORY\", \"TITLE\"]]\n",
    "train_df, val_test_df = train_test_split(extract_df, test_size=0.2, shuffle=True, random_state=2021, stratify=extract_df[\"CATEGORY\"])\n",
    "val_df, test_df = train_test_split(val_test_df, test_size=0.5, shuffle=True, random_state=2021, stratify=val_test_df[\"CATEGORY\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "訓練データ : (10672, 2)\n",
      "検証データ : (1334, 2)\n",
      "テストデータ : (1334, 2)\n"
     ]
    }
   ],
   "source": [
    "print(\"訓練データ : {}\".format(train_df.shape)) #.shape データフレームの行数、列数を取得\n",
    "print(\"検証データ : {}\".format(val_df.shape))\n",
    "print(\"テストデータ : {}\".format(test_df.shape))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "train_df.to_csv(\"NewsAggregatorDataset/train.txt\", sep=\"\\t\", index=None)\n",
    "val_df.to_csv(\"NewsAggregatorDataset/valid.txt\", sep=\"\\t\", index=None)\n",
    "test_df.to_csv(\"NewsAggregatorDataset/test.txt\", sep=\"\\t\", index=None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "b    4502\n",
      "e    4223\n",
      "t    1219\n",
      "m     728\n",
      "Name: CATEGORY, dtype: int64\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
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
    "train_category_var = train_df[\"CATEGORY\"].value_counts()\n",
    "print(train_category_var)\n",
    "train_category_var.plot.bar()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "b    562\n",
      "e    528\n",
      "t    153\n",
      "m     91\n",
      "Name: CATEGORY, dtype: int64\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
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
    "val_category_var = val_df[\"CATEGORY\"].value_counts()\n",
    "print(val_category_var)\n",
    "val_category_var.plot.bar()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "b    563\n",
      "e    528\n",
      "t    152\n",
      "m     91\n",
      "Name: CATEGORY, dtype: int64\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
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
    "test_category_var = test_df[\"CATEGORY\"].value_counts()\n",
    "print(test_category_var)\n",
    "test_category_var.plot.bar()"
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
      "showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#51\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from nltk.corpus import stopwords\n",
    "import nltk\n",
    "nltk.download()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
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
       "      <th>00 bst</th>\n",
       "      <th>05 12</th>\n",
       "      <th>05 12 50</th>\n",
       "      <th>05 12 50 cent</th>\n",
       "      <th>05 12 entertainment</th>\n",
       "      <th>05 12 entertainment solange</th>\n",
       "      <th>05 12 fox</th>\n",
       "      <th>05 12 fox unveils</th>\n",
       "      <th>08 holcim</th>\n",
       "      <th>08 holcim lafarge</th>\n",
       "      <th>...</th>\n",
       "      <th>œf ck youâ cop</th>\n",
       "      <th>œlousyâ lost</th>\n",
       "      <th>œlousyâ lost riverâ</th>\n",
       "      <th>œlousyâ lost riverâ bum</th>\n",
       "      <th>œpiece meatâ</th>\n",
       "      <th>œpiece meatâ fbi</th>\n",
       "      <th>œpiece meatâ fbi denies</th>\n",
       "      <th>œwaist upâ</th>\n",
       "      <th>œwaist upâ star</th>\n",
       "      <th>œwaist upâ star wars</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 157955 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   00 bst  05 12  05 12 50  05 12 50 cent  05 12 entertainment  \\\n",
       "0     0.0    0.0       0.0            0.0                  0.0   \n",
       "1     0.0    0.0       0.0            0.0                  0.0   \n",
       "2     0.0    0.0       0.0            0.0                  0.0   \n",
       "3     0.0    0.0       0.0            0.0                  0.0   \n",
       "4     0.0    0.0       0.0            0.0                  0.0   \n",
       "\n",
       "   05 12 entertainment solange  05 12 fox  05 12 fox unveils  08 holcim  \\\n",
       "0                          0.0        0.0                0.0        0.0   \n",
       "1                          0.0        0.0                0.0        0.0   \n",
       "2                          0.0        0.0                0.0        0.0   \n",
       "3                          0.0        0.0                0.0        0.0   \n",
       "4                          0.0        0.0                0.0        0.0   \n",
       "\n",
       "   08 holcim lafarge  ...  œf ck youâ cop  œlousyâ lost  œlousyâ lost riverâ  \\\n",
       "0                0.0  ...             0.0           0.0                  0.0   \n",
       "1                0.0  ...             0.0           0.0                  0.0   \n",
       "2                0.0  ...             0.0           0.0                  0.0   \n",
       "3                0.0  ...             0.0           0.0                  0.0   \n",
       "4                0.0  ...             0.0           0.0                  0.0   \n",
       "\n",
       "   œlousyâ lost riverâ bum  œpiece meatâ  œpiece meatâ fbi  \\\n",
       "0                      0.0           0.0               0.0   \n",
       "1                      0.0           0.0               0.0   \n",
       "2                      0.0           0.0               0.0   \n",
       "3                      0.0           0.0               0.0   \n",
       "4                      0.0           0.0               0.0   \n",
       "\n",
       "   œpiece meatâ fbi denies  œwaist upâ  œwaist upâ star  œwaist upâ star wars  \n",
       "0                      0.0         0.0              0.0                   0.0  \n",
       "1                      0.0         0.0              0.0                   0.0  \n",
       "2                      0.0         0.0              0.0                   0.0  \n",
       "3                      0.0         0.0              0.0                   0.0  \n",
       "4                      0.0         0.0              0.0                   0.0  \n",
       "\n",
       "[5 rows x 157955 columns]"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#有名なストップワード取得\n",
    "stopwords = stopwords.words('english')\n",
    "\n",
    "tfidf_vectorizer = TfidfVectorizer(stop_words=stopwords, ngram_range=(2,4), min_df=1) \n",
    "\n",
    "#単語の出現頻度を要素とするベクトル\n",
    "#TF-IDF TD:Term Frequency, IDF:Inverse Document Frequency\n",
    "#TfidfVectorizerの出力は2次元の行列が返る、正確にはscipyのオブジェクト\n",
    "#fit()：渡されたデータの最大値、最小値、平均、標準偏差、傾き…などの統計を取得して、内部メモリに保存\n",
    "#transform()：fit()で取得した統計情報を使って、渡されたデータを実際に置き換える\n",
    "#trainデータはそれ自体の統計を基に正規化や欠損値処理を行っても問題ないので、fit_transform()が使える\n",
    "#testデータは、比較的データが少なく、trainデータの統計を使って正規化や欠損値処理を行うべきなので、trainデータに対するfit()の結果で、transform()を行う\n",
    "train_scipy =tfidf_vectorizer.fit_transform(train_df[\"TITLE\"])    \n",
    "val_scipy = tfidf_vectorizer.transform(val_df[\"TITLE\"]) \n",
    "test_scipy = tfidf_vectorizer.transform(test_df[\"TITLE\"]) \n",
    "\n",
    "train_array = train_scipy.toarray()\n",
    "val_array = val_scipy.toarray()\n",
    "test_array = test_scipy.toarray()\n",
    "\n",
    "train_feature_df = pd.DataFrame(data=train_array, columns=tfidf_vectorizer.get_feature_names())\n",
    "val_feature_df = pd.DataFrame(data=val_array, columns=tfidf_vectorizer.get_feature_names())\n",
    "test_feature_df = pd.DataFrame(data=test_array, columns=tfidf_vectorizer.get_feature_names())\n",
    "train_feature_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "#52\n",
    "from sklearn.linear_model import LogisticRegression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LogisticRegression(max_iter=10000, random_state=0)"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#fit(入力値, 目標値)\n",
    "model = LogisticRegression(random_state=0, max_iter=10000)\n",
    "model.fit(train_feature_df, train_df['CATEGORY'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['b' 'e' 'b' ... 'b' 'b' 'e'] [0.33885014 0.6082182  0.58075694 ... 0.58536946 0.65964894 0.60707   ]\n",
      "['b' 'b' 'e' ... 'e' 'b' 'b'] [0.42803394 0.72714936 0.5743209  ... 0.41047372 0.70134806 0.57808968]\n",
      "['b' 'b' 'b' ... 'b' 'e' 'e'] [0.50059491 0.83494612 0.42803394 ... 0.59828999 0.5227727  0.48364209]\n"
     ]
    }
   ],
   "source": [
    "#53\n",
    "import numpy as np\n",
    "\n",
    "def pred_score(model, x):\n",
    "    pred = model.predict(x)\n",
    "    score = np.max(model.predict_proba(x), axis=1)   #axis(軸)\n",
    "    return pred, score\n",
    "\n",
    "train_pred, train_score = pred_score(model, train_feature_df)\n",
    "val_pred, val_score = pred_score(model, val_feature_df)\n",
    "test_pred, test_score = pred_score(model, test_feature_df)\n",
    "print(train_pred, train_score)\n",
    "print(val_pred, val_score)\n",
    "print(test_pred, test_score)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "学習データの正解率： 85.560\n",
      "評価データの正解率： 78.186\n"
     ]
    }
   ],
   "source": [
    "#54\n",
    "from sklearn.metrics import accuracy_score\n",
    "\n",
    "#accurancy_score()ですべてのサンプルのうち正解したサンプルの割合を算出\n",
    "train_accuracy = accuracy_score(train_df['CATEGORY'], train_pred)\n",
    "test_accuracy = accuracy_score(test_df['CATEGORY'], test_pred)\n",
    "\n",
    "print('学習データの正解率： {}'.format(format(train_accuracy*100, '.3f')))\n",
    "print('評価データの正解率： {}'.format(format(test_accuracy*100, '.3f')))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#ゆきさんのコードを参考にさせていただきました"
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
