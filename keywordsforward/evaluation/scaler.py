class MetricScaler:
    @staticmethod
    def cossim_to_10scale(scores, dc=2):
        if isinstance(scores, list):
            return [round((s+1)*5, dc) for s in scores]
        return round((scores+1)*5, dc)