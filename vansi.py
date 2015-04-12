# vansi.py - the main file where all the magic happens

import sys, requests

class Vansi():

	def __init__(self):
		self.wiki_url = "http://en.wikipedia.org/w/api.php?"
		self.wiki_url += "format=json"
		self.wiki_url += "&action=query"
		self.wiki_url += "&rvprop=content"
		self.wiki_url += "&prop=revisions"
		self.user_agent = "Vansi/1.0 (http://vansi.me)"

	def query_wikipedia(self, query):
		url = self.wiki_url + "&titles=" + query
		print url
		try:
			H = {
					'User-Agent': self.user_agent
				}
			resp = requests.post(url).json()
			resp_pages = resp['query']['pages']
			resp_id = resp_pages.itervalues().next()
			resp_revisions = resp_id['revisions'][0]
			return resp_revisions['*']
		except Exception as e:
			print str(e)
			return None

def main():
	vansi = Vansi()
	query_list = sys.argv[1:]
	query = query_list.pop(0)
	for s in query_list:
		query += " "
		query += s
	ans = vansi.query_wikipedia(query)
	ans_paras = ans.split('\n')
	result = ""
	for para in ans_paras:
		sentences = para.split('. ')
		if len(sentences) > 5:
			result += sentences[3]
	result = result.strip('[')
	result = result.strip(']')
	result = result.strip('{')
	result = result.strip('}')
	print result

if __name__ == "__main__":
	main()
