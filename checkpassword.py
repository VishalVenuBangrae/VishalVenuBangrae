import requests
import hashlib
import sys


def request_api_data_pwned(query_char_5):
    url = 'https://api.pwnedpasswords.com/range/' + query_char_5
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f'Error fetching:{res.status_code}, check the api and try again')
    return res


def get_password_leaks_count(hashes_response, hash_to_check_tail):
    hashes_response = (line.split(':') for line in hashes_response.text.splitlines())

    for h, count in hashes_response:

        if h == hash_to_check_tail:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5_char, tail_char = sha1password[:5], sha1password[5:]
    response = request_api_data_pwned(first_5_char)
    return get_password_leaks_count(response, tail_char)


def main(args):
    for password in args:

        count = pwned_api_check(password)

        if count:

            print(f'{password} was found {count} times... Change password!')

        else:

            print(f'{password} was NOT found. Password is safe')

    return 'done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))