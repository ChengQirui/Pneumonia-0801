{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96ceabb4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__' (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)\n",
      "[2022-08-01 17:00:53,381] ERROR in app: Exception on / [GET]\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\cheng\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\app.py\", line 2073, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"C:\\Users\\cheng\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\app.py\", line 1519, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"C:\\Users\\cheng\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\app.py\", line 1517, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"C:\\Users\\cheng\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\app.py\", line 1503, in dispatch_request\n",
      "    return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)\n",
      "  File \"C:\\Users\\cheng\\AppData\\Local\\Temp\\ipykernel_12228\\4098408055.py\", line 26, in init\n",
      "    return(render_template(\"index.html\", result=\"WAITING\"))\n",
      "  File \"C:\\Users\\cheng\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\templating.py\", line 155, in render_template\n",
      "    ctx.app.jinja_env.get_or_select_template(template_name_or_list),\n",
      "  File \"C:\\Users\\cheng\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\jinja2\\environment.py\", line 1068, in get_or_select_template\n",
      "    return self.get_template(template_name_or_list, parent, globals)\n",
      "  File \"C:\\Users\\cheng\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\jinja2\\environment.py\", line 997, in get_template\n",
      "    return self._load_template(name, globals)\n",
      "  File \"C:\\Users\\cheng\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\jinja2\\environment.py\", line 958, in _load_template\n",
      "    template = self.loader.load(self, name, self.make_globals(globals))\n",
      "  File \"C:\\Users\\cheng\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\jinja2\\loaders.py\", line 125, in load\n",
      "    source, filename, uptodate = self.get_source(environment, name)\n",
      "  File \"C:\\Users\\cheng\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\templating.py\", line 59, in get_source\n",
      "    return self._get_source_fast(environment, template)\n",
      "  File \"C:\\Users\\cheng\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\flask\\templating.py\", line 95, in _get_source_fast\n",
      "    raise TemplateNotFound(template)\n",
      "jinja2.exceptions.TemplateNotFound: index.html\n",
      "127.0.0.1 - - [01/Aug/2022 17:00:53] \"GET / HTTP/1.1\" 500 -\n",
      "127.0.0.1 - - [01/Aug/2022 17:00:54] \"GET /favicon.ico HTTP/1.1\" 404 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, request\n",
    "from werkzeug.utils import secure_filename\n",
    "from tensorflow.keras.models import load_model\n",
    "from PIL import Image #use PIL\n",
    "import numpy as np\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/', methods=['GET', 'POST'])\n",
    "def init():\n",
    "    if request.method == 'POST':\n",
    "        file = request.files['file']\n",
    "        print(\"File Received\")\n",
    "        filename = secure_filename(file.filename)\n",
    "        print(filename)\n",
    "        # Open the image form working directory\n",
    "        image = Image.open(file)\n",
    "        model = load_model(\"Pneumonia\")\n",
    "        img = np.asarray(image)\n",
    "        img.resize((150,150,3))\n",
    "        img = np.asarray(img, dtype=\"float32\") #need to transfer to np to reshape\n",
    "        img = img.reshape(1, img.shape[0], img.shape[1], img.shape[2]) #rgb to reshape to 1,100,100,3\n",
    "        pred=model.predict(img)\n",
    "        return(render_template(\"index.html\", result=str(pred)))\n",
    "    else:\n",
    "        return(render_template(\"index.html\", result=\"WAITING\"))\n",
    "if __name__ == \"__main__\":\n",
    "    app.run()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1ed93c62",
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
   "version": "3.8.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
