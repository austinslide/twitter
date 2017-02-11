#doesnt work in isolation! code block for generating json of word frequency for d3 viz
import vincent

word_freq = count_terms_only.most_common(20)
labels, freq = zip(*word_freq)
data = {'data': freq, 'x': labels}
bar = vincent.Bar(data, iter_idx='x')
bar.to_json('data/term_freq.json')
