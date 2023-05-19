
# factors

## Summary
- Author: Lucius Chee Zihan
- Discord Tag: lcz5#3392
- Category: Cryptography
- Difficulty: Medium

## Solution
Note: this file includes equations written in LaTEX.
In the files provided, we see an encrypted file, a public key file, and files containing the key generation script.
From the capitalisation of the challenge description, we can deduce this has something to do with one of Fermat's theorems.
We shall look into the key generation script (keygen.py and primes.py)
We see this function in `primes.py`:
```python
def generate_prime_candidate(length):
    a = 0b1 << (length-1) 
    p = randrange(
            a,
            a + 1180591620717411303425
        )
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p
```
It seems like the prime is generated between $$2^{2048}$$ and $$2^{2048}$$ + 1180591620717411303425 (with the LSB set to 1 to ensure oddness)
In RSA, we need to generate `p` and `q`, prime factors of `n`.
The security of the key depends on the fact that `n` is hard to factorise.
However, the factors are closer than $$2^{100}$$ from each other.
We can thus use Fermat's factorisation method to factor the number.
Fermat's factorisation method states that an odd integer is factorisable to the difference of 2 squares:
```math
N = a^2 - b^2
```
which can be factored into:
```math
N = (a-b)(a+b)
```
Hence, `a-b` and `a+b` is `p` and `q`, in no specific order.

Knowing this, we can use RsaCTFTool to crack the key:
```
python3.9 RsaCtfTool.py --publickey pubkey.pem --attack fermat --private                                                  
[*] Testing key pubkey.pem.
[*] Performing fermat attack on pubkey.pem.
[*] Attack success with fermat method !

Results for pubkey.pem:

Private key :
-----BEGIN RSA PRIVATE KEY-----
MIILJQIBAAKCAgBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

...
```
We have derived the private key, let us go decrypt the file.
![image](https://i.ibb.co/MDZvbVD/Screenshot-2023-05-19-231431.png)




## Flag
```
YCEP2023{don't_choose_your_factors_too_close}
```

## Additional notes 
Credits/sources:
Prime generation script was derived from https://medium.com/@ntnprdhmm/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb
