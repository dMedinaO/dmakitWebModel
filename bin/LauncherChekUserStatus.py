'''
script que permite la revision de los usuarios en estado cancelado:

Obtiene los usuarios
Obtiene y elimina los job (base de datos y areas de trabajo)
Elimina los usuarios de la BD
'''

from modulesProject.user_module import deleteUsers

deleteObject = deleteUsers.deleteUsers()

deleteObject.getCanceledUsers()

#por cada usuario obtenemos los jobs
for user in deleteObject.ListUserRemove:
    listJobs = deleteObject.getJobsUser(user)

    #por cada job lo eliminamos y removemos el directorio
    for job in listJobs:
        print "remove job: ", job
        deleteObject.deleteJob(job, user)
    #eliminamos el area de trabajo...
    deleteObject.removeAreaJob(user)
