from Crypto.Util.number import long_to_bytes

def wiener(e, n):
    # Convert e/n into a continued fraction
    cf = continued_fraction(e/n)
    convergents = cf.convergents()
    for kd in convergents:
        k = kd.numerator()
        d = kd.denominator()
        # Check if k and d meet the requirements
        if k == 0 or d%2 == 0 or e*d % k != 1:
            continue
        phi = (e*d - 1)/k
        # Create the polynomial
        x = PolynomialRing(RationalField(), 'x').gen()
        f = x^2 - (n-phi+1)*x + n
        roots = f.roots()
        # Check if polynomial as two roots
        if len(roots) != 2:
            continue
        # Check if roots of the polynomial are p and q
        p,q = int(roots[0][0]), int(roots[1][0])
        if p*q == n:
            return d
    return None
# Test to see if our attack works
if __name__ == '__main__':
    n = 6727075990400738687345725133831068548505159909089226909308151105405617384093373931141833301653602476784414065504536979164089581789354173719785815972324079
    e = 4805054278857670490961232238450763248932257077920876363791536503861155274352289134505009741863918247921515546177391127175463544741368225721957798416107743
    c = 5928120944877154092488159606792758283490469364444892167942345801713373962617628757053412232636219967675256510422984948872954949616521392542703915478027634
    d = wiener(e,n)
    assert not d is None, "Wiener's attack failed :("
    print(long_to_bytes(int(pow(c,d,n))).decode())
