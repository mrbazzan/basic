
class Example:
    def divide(self, v):
        result = 100/v
        return result

    def interpolate(self, *args):
        result = "%s is %s" % args
        return result


if __name__ == "__main__":
    import pdb
    pdb.set_trace()

    e = Example()
    print(e.divide(0))

    print("-"*80)
    print(e.interpolate('Chi', 'very', 'cool'))

