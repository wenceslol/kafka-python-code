import random
import string

user_ids = list(range(1, 101))
recipient_ids = list(range(1, 101))


def generate_message() -> dict:
    random_user_id = random.choice(user_ids)

    #Copia a array de recipientes
    recipient_ids_copy = recipient_ids.copy()

    #Usuário não pode enviar mensagens a si mesmo
    recipient_ids_copy.remove(random_user_id)
    random_recipient_id = random.choice(recipient_ids_copy)

    #Gera uma mensagem aleatória
    message = ''.join(random.choice(string.ascii_letters) for i in range(32))

    return{
        'user_id': random_user_id,
        'recipient_id': random_recipient_id,
        'message': message
    }

#teste
#if __name__ == '__main__':
#    print(generate_message())