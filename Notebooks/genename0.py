{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ce1f0d8f-d65a-4aa2-b6cf-83e2097c2abf",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: '-f'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_24737/2302612711.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     15\u001b[0m                 \u001b[0mmyfile01\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwrite\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf'{fileX}\\n'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     16\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 17\u001b[0;31m \u001b[0mgene_namez\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/tmp/ipykernel_24737/2302612711.py\u001b[0m in \u001b[0;36mgene_namez\u001b[0;34m()\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mgene_namez\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m     \u001b[0;32mwith\u001b[0m \u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfileX_input\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mmyfile\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      7\u001b[0m         \u001b[0;32mwith\u001b[0m \u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfileX_output\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m'w'\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mmyfile01\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m             \u001b[0mfetche_file\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmyfile\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mreadlines\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: '-f'"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "fileX_input=sys.argv[1]\n",
    "fileX_output=sys.argv[2]\n",
    "\n",
    "def gene_namez():\n",
    "    with open(fileX_input) as myfile:\n",
    "        with open(fileX_output,'w') as myfile01:\n",
    "            fetche_file = myfile.readlines()\n",
    "            xz=fetche_file[33:]\n",
    "            for x in xz:\n",
    "                fileX=x.split(\" \")[0]\n",
    "                if fileX.startswith('-'):\n",
    "                    break\n",
    "                #print(f)\n",
    "                myfile01.write(f'{fileX}\\n')\n",
    "\n",
    "gene_namez()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df64c8bc-e80f-42e2-a1c6-97afd804e205",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6c17850d-c000-4fed-ac35-27918da31ced",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
