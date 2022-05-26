# sample: ff908727cc1b5335e541fbcd80a327565f308bc7
from datetime import date, timedelta
import base64
keys = (
    ('iota', 'bcmp', 'jorh', 'adgn', 'nqta', 'lqty', 'hwbg', 'ilqe', 'orub', 'fuze', 'rwzj', 'jmpw', 'kpsx', 'aein', 'uxch', 'mrdu', 'akns', 'nqva', 'mrdv', 'rwam', 'qthy', 'yblq', 'ilqe', 'rehy', 'qtfw', 'lorf', 'jmqv', 'hlou', 'zcgl', 'tfuz', 'jmpd', 'orub'),
    ('fxcj', 'egxa', 'ndgy', 'duze', 'orwb', 'hmpu', 'aejo', 'fuze', 'knsg', 'mpsx', 'dhmq', 'euxc', 'knqg', 'qdgx', 'ailq', 'vyin', 'jnsx', 'dglq', 'ydgl', 'hwbg', 'rehz', 'bjot', 'uybm', 'gjmt', 'zehm', 'xcgl', 'clqd', 'lorh', 'zclr', 'uxbl', 'orwb', 'kpsx'),
    ('vdjq', 'oruz', 'nthy', 'clqd', 'loty', 'mpty', 'jmrw', 'cglp', 'fuxc', 'ckod', 'zcmr', 'knsx', 'aehn', 'zehm', 'xadi', 'xadk', 'seva', 'imqe', 'txcl', 'bfio', 'xadi', 'tgwb', 'sehy', 'knsg', 'psxc', 'knsx', 'mpdu', 'qduz', 'xaip', 'qvyi', 'kosx', 'losy'),
    ('dinu', 'eglo', 'mrdw', 'lqtv', 'ckpd', 'cgkp', 'quyi', 'vyin', 'qvyi', 'vycn', 'osxc', 'loty', 'ilot', 'adgl', 'wbej', 'sehy', 'jnrf', 'zjnr', 'ruyj', 'hlqu', 'ybel', 'dhwb', 'jmpd', 'xbjo', 'pswb', 'zehm', 'dgxc', 'orfw', 'psgx', 'uxaf', 'aehm', 'ehmr'),
    ('wcmt', 'ikpu', 'orwi', 'fknu', 'zehn', 'pswc', 'qehz', 'mpsx', 'swak', 'uxam', 'fimr', 'uxch', 'xakp', 'mpdu', 'ails', 'svyk', 'adin', 'nqth', 'jnsg', 'mrva', 'ejmr', 'mqeu', 'zjmr', 'orwb', 'bejo', 'dgwc', 'twbl', 'hkou', 'uxch', 'rdgx', 'vzjn', 'bfjo'),
    ('qbgo', 'wyej', 'uxci', 'vyin', 'adgn', 'waej', 'nsfw', 'nrdu', 'nrfv', 'aimr', 'uxak', 'dhkp', 'xadi', 'gvaf', 'lpsg', 'yblq', 'twak', 'rvyi', 'qtyi', 'orvb', 'bejo', 'reuz', 'wzcm', 'rtyc', 'gjmr', 'behm', 'zcmr', 'lorf', 'uxbk', 'uxbm', 'pswb', 'zchm'),
    ('pdha', 'gjmr', 'insh', 'qthy', 'orev', 'fvyd', 'vybg', 'hwze', 'qtfw', 'yblq', 'orwb', 'cgjo', 'mptg', 'zcmr', 'ruzj', 'vzcm', 'impu', 'knqv', 'mpsx', 'adhl', 'ychl', 'xafk', 'dgva', 'ilpt', 'ilqe', 'ilqe', 'loty', 'vybl', 'jnqv', 'jmpd', 'pthx', 'orfw'),
    ('xejr', 'txak', 'fwbh', 'xafk', 'seva', 'cfin', 'adin', 'dhkp', 'vycg', 'ptgx', 'ailq', 'gjns', 'vybg', 'ilot', 'ilot', 'bjnt', 'mquz', 'ehlp', 'hwze', 'tfwb', 'jmpd', 'korf', 'jmpf', 'wzjo', 'wzjo', 'mpsx', 'uxch', 'sfuz', 'rdgx', 'nrdu', 'aimr', 'uxak'),
    ('ewdj', 'behm', 'takp', 'ejmt', 'zdgm', 'lqty', 'hlqu', 'gjmr', 'rduz', 'loth', 'swbk', 'knrw', 'gvze', 'zckp', 'impu', 'nqua', 'mrfx', 'ilqe', 'psgx', 'cfip', 'fils', 'nqva', 'qvyi', 'xain', 'losy', 'loty', 'dglq', 'xadi', 'ehxb', 'loth', 'seva', 'jnsf'),
    ('tyio', 'ehkp', 'ehyd', 'knsg', 'knsx', 'nqva', 'adgl', 'vybg', 'knqe', 'orva', 'wzdi', 'mqev', 'ptyi', 'gjot', 'hwbg', 'bjmr', 'swbk', 'fjmr', 'mpsx', 'ruxc', 'mpuz', 'psxc', 'ruxc', 'svzj', 'uxcm', 'zcmr', 'nrva', 'ruzj', 'svzk', 'quxc', 'puxc', 'knqv'),
    ('hzel', 'gvzf', 'lotz', 'loty', 'ails', 'svyk', 'gjnt', 'vybi', 'bjot', 'vybn', 'gjot', 'wzdj', 'rduz', 'pthy', 'jmpd', 'psxc', 'swzk', 'chkp', 'vaej', 'xaek', 'nrfv', 'ckpd', 'svak', 'fkns', 'ilqv', 'psxc', 'lpdu', 'psgx', 'nqev', 'ilqe', 'bkpt', 'twal'),
    ('wbmt', 'vzcm', 'ptyk', 'ckpd', 'ruzj', 'mpsz', 'hkou', 'sfwa', 'uxcm', 'dhkq', 'afin', 'qdgx', 'bfin', 'nqth', 'ilot', 'nqev', 'ruyi', 'ybel', 'jorf', 'aeho', 'fuxc', 'ruxc', 'uxch', 'nqdv', 'lpsy', 'hxbg', 'ybfk', 'nqev', 'orvb', 'fwze', 'blot', 'oruz'),
)


month_keys = "NSLWBKZODEPV"
def generate_domains(start_date, end_date):
    """
    Generate domains for specified date range
    """
    # generated domain is base64 encoded with a custom character set
    # create translation table
    trans = ''.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=', 
        'ghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZabcdefz0123456789+/=')
    dt = start_date
    while dt <= end_date:
        # date is converted into following 4 character format:
        # '<dd> <char for month> <year's last digit>'
        # e.g. '31V2'
        dt_key = f'{dt.day:02}{month_keys[dt.month - 1]}{dt.year % 10}'
        # the 4 character format is then xor'ed by a unique key determined by
        # current date. also 4 characters.
        xor_key = keys[dt.month - 1][dt.day - 1]
        domain = [ord(x) ^ ord(y) for x, y in zip(dt_key, xor_key)]
        # hex encode (uppercase) and prepend 'nuu'
        domain = 'nuu' + bytes(domain).hex().upper()
        domain = domain.encode('ascii')
        # base64 encode and translate to custom characters, then remove padding char
        domain = base64.b64encode(domain).decode('ascii').translate(trans)
        domain = domain.replace('=', '').lower() + '.freedynamicdns.org'
        yield (dt, domain, dt_key, xor_key)
        dt += timedelta(days=1)


if __name__ == '__main__':
    for (dt, domain, dt_key, xor_key) in generate_domains(date(2022, 1, 1), date(2022, 12, 31)):
        print(dt, domain, dt_key, xor_key)
