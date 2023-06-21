{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4c6b8b98-610e-47fb-903f-9253c5dcf0c1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/Users/annikagilles/Documents/ITM Demo/demo-itm/Cynthia Erivo - At Last.mp4'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from pytube import YouTube\n",
    "\n",
    "yt = YouTube('https://www.youtube.com/watch?v=HUwhPN5-9bk')\n",
    "\n",
    "yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()"
   ]
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
