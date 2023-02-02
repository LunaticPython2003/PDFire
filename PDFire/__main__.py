import os
if __name__ == '__main__':
    os.chdir('PDFire/static')
    if os.path.exists('setup') is False:
        print("Performing first time setup \n")
        with open('setup', 'w') as fp:
            pass
        os.system('npm install')
        os.chdir('../..')
        os.system('pip install -r requirements.txt')
        os.chdir('PDFire')
    else:
        print("Requirement already satisfied, running the project \n")
        os.chdir("..")
    os.system('python3 -m flask --app main --debug run')