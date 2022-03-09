from zdppy_random import Random

r = Random(debug=True)

for _ in range(10):
    r.log.info(r.random_str(16))
    r.log.info(r.random_str(32))
    r.log.info(r.random_str(64))
    r.log.info(r.random_str(128))
