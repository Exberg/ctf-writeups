# ctf-writeups
im still a beginner for haccer...
this is my first time doing ctf-writeups for pico-ctf, so the below is kinda funny.

---

#### Scan Surprise
![easiest](https://github.com/Exberg/ctf-writeups/blob/main/images/image1.png)

this was the easiest thing ive done, just unzip files, open image and scan qr code.

---

### Verify
Author: Jeffery John
Description
People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.

<img width="576" alt="Screenshot 2024-12-12 at 2 02 31 AM" src="https://github.com/user-attachments/assets/00fca880-5602-4e9a-b59b-54b3d509d098" />

first thing first, open linux and run the script. 

<img width="1059" alt="Screenshot 2024-12-12 at 2 06 28 AM" src="https://github.com/user-attachments/assets/37880966-5911-4c24-b023-e39b5a210fd8" />

After ls the files, i figured i can just loop them instead of checking one by one since its so tedious to do so.

---

### information
![cat](https://github.com/user-attachments/assets/70e6f365-eddd-4619-8da2-a2b0806d413c)

This is prob the hardest ive done, because when i actually looked at the hint.
Spoilers Alert: "look at the file" NOT THE CAT!

<img width="983" alt="Screenshot 2024-12-12 at 2 23 53 AM" src="https://github.com/user-attachments/assets/249dc373-451f-4182-a5d4-ae66f6ddc9f9" />

So, i used exiftool to extract some juicy infos. At the beginning, i was like where's the answer??? But when i take a deep look, and i paste everything into the cyberchef, i found this particular line (highlighted in green) delivered me straight to the answer :P

---

### what's a net cat?
`
Using netcat (nc) is going to be pretty important. Can you connect to jupiter.challenges.picoctf.org at port 64287 to get the flag?
`

I find this interesting because of the title lol

First, install netcat on terminal. Then, Connect to the Host and Port: nc jupiter.challenges.picoctf.org 64287

<img width="347" alt="Screenshot 2024-12-12 at 2 36 52 AM" src="https://github.com/user-attachments/assets/67c31a19-66de-46fc-90c4-0e97a9393968" />

**so ezzZ = =**
