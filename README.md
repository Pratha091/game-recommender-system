# game-recommender-system

This is a content based movie recommender system using cosine similarity which will recommend you 5 most similar games to the game you have chosen from the list.

Technoligies Used:
1. API - Data is fetched from RAWG API
2. Jupyter Notebook - Data is preprocessed in jupyter notebook.
3. Python language
4. Pycharm Editor
5. Streamlit framework

## Installation guide for project:
### Clone project into local system
The clone command copies a project form an existing remote Github repository to your local repository.
Follow these steps to clone a project from a remote git repository to your local repository:

1. Login into your Github account at https://www.github.com.
2. After you have logged-in, click on the project you want to clone.
3. On the project page, click on the clone button, a dropdown will be shown with options to clone with HTTPS and SSH. Select clone with HTTPS and copy the address.
4. Next, open terminal and go to the directory where you want to copy the project. Use the following command to clone the project:

 git clone https://github.com/Pratha091/game-recommender-system.git
  
5. Next, navigate inside the cloned project folder
  
 cd project-folder

### Before you get started, you're going to need a few things:

1. Your favorite IDE or text editor
2. Python 3.7 - Python 3.10 (https://www.python.org/downloads/)
3. PIP (https://pip.pypa.io/en/stable/installation/)
  
### Install Streamlit on Windows
Streamlit's officially-supported environment manager on Windows is Anaconda Navigator(https://docs.anaconda.com/anaconda/install/windows/).
  
### Create a new environment with Streamlit
Next you'll need to set up your environment.

1. Follow the steps provided by Anaconda to set up and manage your environment using the Anaconda Navigator.(https://docs.anaconda.com/anaconda/navigator/getting-started/#managing-environments)

2. Select the "▶" icon next to your new environment. Then select "Open terminal":

  ![image](https://user-images.githubusercontent.com/84763662/170879928-cb305696-5d20-476b-90c3-74b685dc428e.png)
  
  
3. In the terminal that appears, type:
  
pip install streamlit
  
Test that the installation worked:

streamlit hello
  
Streamlit's Hello app should appear in a new tab in your web browser!
  
### Use your new environment
1. In Anaconda Navigator, open a terminal in your environment (see step 2 above).

2. In the terminal that appears, use Streamlit as usual:

streamlit run myfile.py
