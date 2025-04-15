import buildbot
import buildbot.process.factory
from buildbot.steps.shell import WithProperties
from buildbot.steps.trigger import Trigger
from buildbot.schedulers import basic, timed, triggerable
from buildbot.steps import source

def runboost(config_options):
    f = buildbot.process.factory.BuildFactory()
    # Determine the build directory.
    getBuildDir(f)
    f = setProperty(f, 'use_path', WithProperties('%(builddir)s/clang-install/usr/local/bin'))
    cleanCompilerDir(f)
    # pull test-suite
    pullboostrunner(f)
    #Download compiler artifacts to be used for this build
    GetCompilerArtifacts(f)
    # run tests
    # runner=llvmlab
    # BOOST_ROOT=builddir/boost
    # echo using borland : "integration" : %CD:\=/%/integration/bin/bcc32 : ; > %MYJAMFILE%
    f.addStep(buildbot.steps.shell.ShellCommand(
              name='user-config.jam',
              command=['echo', 'using', 'clang', ':', 'darwin-4.2.1', ':', 
                       WithProperties('%(use_path)s/clang'), ':', config_options, 
                       ';', '>', 'user-config.jam'],
              haltOnFailure=True,
              description=['create user-config.jam'],
              workdir='.',
              ))
    #--bjam-options=target-os=windows --bjam-options=-l300 --bjam-options=--debug-level=3 --bjam-options=--user-config=%MYJAMFILE% --have-source --skip-script-download --ftp=ftp://boost:5pelV8XUxfO3@ftp.lizardconman.net >runner.log
    f.addStep(buildbot.steps.shell.ShellCommand(
              name='run.py',
              command=['python', 'boost_runner/run.py', WithProperties('--tag=%(boost_tag)s'), 
                       '--runner=llvmlab', '--bjam-options=--toolset=clang-darwin', 
                       WithProperties('--bjam-options=--user-config=%(builddir)s/userconfig.jam'),
                       '--ftp=ftp://boost:5pelV8XUxfO3@ftp.lizardconman.net',
                       WithProperties('--bjam-options=-j%(jobs)s'),'--user=""',],
              haltOnFailure=True,
              description=['boost regression harness'],
              workdir='.',
              timeout=14400
              ))
    return f
