import json, datetime, urllib.request, ssl


class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):
        # TODO
        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise
        with open('ratios.json') as f:
            json_data = json.loads(f.read())
        today=datetime.date.today()
        
        for ratios in json_data:
            if ratios['base_currency'] == self.base and ratios['target_currency'] == self.target and ratios['date_fetched'] == today.strftime('%Y-%m-%d'):
                return True
        else:
            return False
        pass

    def fetch_ratio(self):
        # TODO
        # This function calls API for today's exchange ratio
        # Should ask API for today's exchange ratio with given base and target currency
        # and call save_ratio method to save it
        ctx=ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        url=('http://api.exchangerate.host/live?access_key=cffa089eb163fa5a87eaded7c524a1a9&source={}').format(self.base)
        response_api=urllib.request.urlopen(url)
        data_from_api=response_api.read()
        data_json = json.loads(data_from_api.decode('utf-8'))
        temp="{}{}".format(self.base,self.target)
        ratio=data_json["quotes"][temp]
        self.save_ratio(ratio)
        pass

    def save_ratio(self, ratio):
        # TODO
        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)
        with open('ratios.json') as f:
            json_data=json.loads(f.read())
        today=datetime.date.today()
        for ratios in json_data:
            if ratios['base_currency'] == self.base and ratios['target_currency'] == self.target:
                ratios['ratio']=ratio
                with open('ratios.json', 'w') as f:
                    f.write(json.dumps(json_data, indent=2))
                break
                
        else:
            exchange = {'base_currency': self.base,'target_currency': self.target,'date_fetched': today.strftime('%Y-%m-%d'), 'ratio': ratio}
            json_data.append(exchange)
            with open('ratios.json', 'w') as f:
                f.write(json.dumps(json_data, indent=2))
        pass

    def get_matched_ratio_value(self):
        # TODO
        # Should read file and receive exchange rate for given base and target currency from that file
        with open('ratios.json') as f:
            json_data = json.loads(f.read())
        for ratios in json_data:
            if ratios['base_currency'] == self.base and ratios['target_currency'] == self.target:
                return ratios['ratio']
        else:
            return False
        pass
