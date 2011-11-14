#!/usr/bin/env python

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

'''This examples shows how to submit a single job a GRAM 
   jobmanager using the 'pythonic' version of the API. 
'''

__author__    = "Ole Christian Weidner"
__email__     = "ole.weidner@me.com"
__copyright__ = "Copyright 2011, Ole Christian Weidner"
__license__   = "MIT"

import bliss.saga as saga

def main():
    
    try: 
        # start a local job service
        js = saga.job.Service("gram://eric1.loni.org/jobmanager-fork")

        # describe our job
        jd = saga.job.Description()
        jd.set_attribute("Executable", '/bin/sleep')
        jd.arguments = ["10"]
        jd.output = "gramjob.stdout"
        jd.error  = "gramjob.stderr"

        print jd.get_vector_attribute("Arguments")

        # create & run the job
        myjob = js.create_job(jd)

        print "Job State : %s" % (myjob.get_state())

        myjob.run()

        print "Job ID    : %s" % (myjob.jobid)
        print "Job State : %s" % (myjob.get_state())
        
        print "...waiting for job..."
        myjob.wait()

        print "Job State : %s" % (myjob.get_state())
        print "Exitcode  : %s" % (myjob.get_attribute("Exitcode"))

    except saga.Exception, ex:
        print "Oh, snap! An error occured: %s" % (str(ex))
        print "Traceback: %s" % ex.traceback

if __name__ == "__main__":
    main()
