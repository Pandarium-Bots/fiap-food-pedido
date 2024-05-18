import requests

def check_sonar_status(url, username, password):
    try:
        response = requests.get(f'{url}/api/system/status', auth=(username, password))
        response.raise_for_status()
        
        status = response.json().get('status', 'UNKNOWN')
        return status == 'UP'
    except requests.exceptions.RequestException as e:
        print(f'Error checking SonarQube status: {e}')
        return False

if __name__ == '__main__':
    sonar_url = 'http://localhost:9000'  # Substitua pelo URL do seu SonarQube
    sonar_username = 'seu_username'      # Substitua pelo seu nome de usuário
    sonar_password = 'seu_password'      # Substitua pela sua senha

    if check_sonar_status(sonar_url, sonar_username, sonar_password):
        print('SonarQube está rodando.')
    else:
        print('SonarQube não está rodando.')
