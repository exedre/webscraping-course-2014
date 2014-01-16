from webscraping import webkit
w = webkit.WebkitBrowser(gui=True,proxy='')

html = w.get('http://duckduckgo.com')
w.fill('input[id=search_form_input_homepage]', 'webscraping')
w.screenshot('duckduckgo_search.jpg')
w.click('input[id=search_button_homepage]')

w.wait(10)
w.screenshot('duckduckgo_results.jpg')

html = w.current_html()

w.get('http://google.com')
w.fill('input[name=q]', 'webscraping')
w.screenshot('google_search.jpg')


w.click('input[name=btnG]')
w.wait(40)
w.screenshot('google_results.jpg')


