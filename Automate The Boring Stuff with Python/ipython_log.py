# IPython log file

get_ipython().magic('logstart')
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n+1):
        total *= i 
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s', (total))
    return total

logging.debug('End of program')

print(factorial(5))
get_ipython().magic('logstart')
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n+1):
        total *= i 
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s', (total))
    return total

logging.debug('End of program')

print(factorial(5))
get_ipython().magic('logstop')
get_ipython().magic('logstart')
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n+1):
        total *= i 
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s', (total))
    return total

logging.debug('End of program')

print(factorial(5))
import logging
get_ipython().magic('logstart')
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n+1):
        total *= i 
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s', (total))
    return total

logging.debug('End of program')

print(factorial(5))
get_ipython().magic('logstop')
import logging
get_ipython().magic('logstart')
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n+1):
        total *= i 
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s', (total))
    return total

logging.debug('End of program')

print(factorial(5))
get_ipython().magic('logstop')
# Let's log some info to find out what's going wrong.
import logging
reload(logging)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# Uncomment the next line to disable logging messages
# logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n+1):
        total *= i 
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s', (total))
    return total

logging.debug('End of program')

print(factorial(5))
# Let's log some info to find out what's going wrong.
import logging
imp.reload(logging)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# Uncomment the next line to disable logging messages
# logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n+1):
        total *= i 
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s', (total))
    return total

logging.debug('End of program')

print(factorial(5))
# Let's log some info to find out what's going wrong.
import logging
importlib.reload(logging)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# Uncomment the next line to disable logging messages
# logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n+1):
        total *= i 
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s', (total))
    return total

logging.debug('End of program')

print(factorial(5))
# Let's log some info to find out what's going wrong.
import logging
logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.DEBUG)



# Uncomment the next line to disable logging messages
# logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n+1):
        total *= i 
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s', (total))
    return total

logging.debug('End of program')

print(factorial(5))
# Let's log some info to find out what's going wrong.
import logging
logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
#logger.addHandler(fhandler)
logger.setLevel(logging.DEBUG)



# Uncomment the next line to disable logging messages
# logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n+1):
        total *= i 
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s', (total))
    return total

logging.debug('End of program')

print(factorial(5))
# Let's log some info to find out what's going wrong.
import logging
logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#fhandler.setFormatter(formatter)
#logger.addHandler(fhandler)
logger.setLevel(logging.DEBUG)



# Uncomment the next line to disable logging messages
# logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n+1):
        total *= i 
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s', (total))
    return total

logging.debug('End of program')

print(factorial(5))
# Let's log some info to find out what's going wrong.
import logging
logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#fhandler.setFormatter(formatter)
#logger.addHandler(fhandler)
shandler = logging.StreamHandler()

logger.setLevel(logging.DEBUG)



# Uncomment the next line to disable logging messages
# logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n+1):
        total *= i 
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s', (total))
    return total

logging.debug('End of program')

print(factorial(5))
# Let's log some info to find out what's going wrong.
import logging
logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#fhandler.setFormatter(formatter)
#logger.addHandler(fhandler)
shandler = logging.StreamHandler()
shandler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)



# Uncomment the next line to disable logging messages
# logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n+1):
        total *= i 
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s', (total))
    return total

logging.debug('End of program')

print(factorial(5))
# Let's log some info to find out what's going wrong.
import logging
logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#fhandler.setFormatter(formatter)
#logger.addHandler(fhandler)
shandler = logging.StreamHandler()
logger.addHandler(shandler)
shandler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)



# Uncomment the next line to disable logging messages
# logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n+1):
        total *= i 
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s', (total))
    return total

logging.debug('End of program')

print(factorial(5))
# Let's log some info to find out what's going wrong.
import logging
logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
shandler = logging.StreamHandler()
logger.addHandler(shandler)
shandler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)



# Uncomment the next line to disable logging messages
logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n+1):
        total *= i 
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s', (total))
    return total

logging.debug('End of program')

print(factorial(5))
# Let's log some info to find out what's going wrong.
import logging
logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
shandler = logging.StreamHandler()
logger.addHandler(shandler)
shandler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)



# Uncomment the next line to disable logging messages
# logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n+1):
        total *= i 
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s', (total))
    return total

logging.debug('End of program')

print(factorial(5))
# Let's log some info to find out what's going wrong.
import logging
logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
shandler = logging.StreamHandler()
logger.addHandler(shandler)
shandler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)



# Uncomment the next line to disable logging messages
# logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n+1):
        total *= i 
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s', (total))
    return total

logging.debug('End of program')

print(factorial(5))
get_ipython().magic('logstart')
# Let's log some info to find out what's going wrong.
import logging
logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
shandler = logging.StreamHandler()
logger.addHandler(shandler)
shandler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)



# Uncomment the next line to disable logging messages
# logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n+1):
        total *= i 
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s', (total))
    return total

logging.debug('End of program')

print(factorial(5))
get_ipython().magic('logstop')
