class: CommandLineTool
cwlVersion: v1.0
$namespaces:
  cwltool: "http://commonwl.org/cwltool#"
inputs:
  sleep_time:
    type: int
    default: 3
    inputBinding: {}
outputs: []
requirements:
  cwltool:TimeLimit:
    timelimit: 15
baseCommand: sleep
