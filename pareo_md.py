import pickle

def main():
    with open('pareo.pkl', 'rb') as file:
        title_url = pickle.load(file)

    # modifying
    for i in range(len(title_url)):
        if '# ' in title_url[i][0]:
            title_url[i] = (title_url[i][0].replace('# ', '#'), title_url[i][1])
        if '＃' in title_url[i][0]:
            title_url[i] = (title_url[i][0].replace('＃', '#'), title_url[i][1])
        if '＃ ' in title_url[i][0]:
            title_url[i] = (title_url[i][0].replace('＃ ', '#'), title_url[i][1])

    data = []
    for title, url in title_url:
        data.append((zero_dec(title), url))

    data.sort(key=lambda x: x[0])


    with open("README.md", "w") as f:
        f.write('# パレオなチャンネル\n\n')
        for i, (title, link) in enumerate(data):
            true_link = 'https://ch.nicovideo.jp/' + link
            f.write(f'{i+1}. [{title}]({true_link})\n')



def zero_dec(words):
    flag = False
    dec = ''
    for w in words:
        if w == '#':
            flag = True
            continue
        if w.isdecimal() == False:
            flag = False

        if flag == True:
            dec += w

    if len(dec) == 1:
        new = words.replace('#'+ dec, '#0' + dec)
    else:
        new = words

    return new



if __name__ == '__main__':
    main()