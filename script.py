per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input('введите величину депозита'))

tcb_d = int((per_cent['ТКБ']) * (money/100))
per_cent['ТКБ']=(tcb_d)
skb_d= int((per_cent['СКБ']) * (money/100))
per_cent['СКБ']=(skb_d)
vtb_d = int((per_cent['ВТБ']) * (money/100))
per_cent['ВТБ']=(vtb_d)
sber_d = int((per_cent['СБЕР']) * (money/100))
per_cent['СБЕР']=(sber_d)

for keys in per_cent:
 print ("Банк: %s, Депозит: %s" % (keys, per_cent[keys]))

 max_value = max([(value, key) for key, value in per_cent.items()])
print ('Максимальная сумма, которую вы можете заработать -', max_value[0],'от банка', max_value[1])
