<<COMMENT1
  This script will run all or only specified by tag tests
COMMENT1

run_test() {

  if [ "$behavetags" = "" ] && [ "$junit" = "true" ] ; then
    behave $testlocation --junit --junit-directory $resultslocation
    junit-viewer --results=resultslocation --save=$reportnameabsoluteName
  elif [ "$behavetags" = "" ] && [ "$junit" = "false" ] ; then
    behave $testlocation
  elif [ "$behavetags" != "" ] && [ "$junit" = "true" ] ; then
    echo "Running behave scenario $behavetags"
    behave $testlocation --tags=$behavetags --junit --junit-directory $resultslocation
    #echo "Running junit-viewer --results=$resultslocation --save=$reportnameabsoluteName"
    #junit-viewer --results=$resultslocation --save=$reportnameabsoluteName
  elif [ "$behavetags" != "" ] && [ "$junit" = "false" ] ; then
    behave $testlocation --tags=$behavetags
  fi

}

export_to_hiptest() {
  echo "Exporting to HipTest"
  for file in "$resultslocation/*.xml"
  do
    echo $file
    echo "$hiptestconfigfile/hiptest-publisher.config"
    #hiptest-publisher --config-file "$hiptestconfigfile/hiptest-publisher.config" --push "$file"  --push-format junit
  done
}

main_method() {
  lchr=${resultslocation#$resultslocation%?}}

  DATETIMESTAMP=$(date +'%Y%m%d%H%M%S')
  DATETIMESTAMP="${DATETIMESTAMP%|*}"

  reportnameabsoluteName="${resultslocation}/${reportname}-${DATETIMESTAMP}.html"

  if [ "$lchr" != "/" ] ; then
    reportnameabsoluteName="${resultslocation}/${reportname}-${DATETIMESTAMP}.html"
  else
    reportnameabsoluteName="${resultslocation}html/${reportname}-${DATETIMESTAMP}.html"
  fi

  run_test

  if [ "$hiptest" = "true" ] ; then
    export_to_hiptest
  fi
}

# Parse the command-line arguments
while [ "$#" -gt "0" ]; do
  case "$1" in
    -tl|--testlocation)
      # feature location
      testlocation="$2"
      if ! [ -d "$testlocation" ] ; then
        echo "Error: Test location $testlocation does not exists. Exiting."
        exit -1
      fi
      shift 2
    ;;
    -t|--tags)
      # scenario tags
      behavetags="$2"
      shift 2
    ;;
    -j|--junit)
      # Create junit output
      junit="$2"
      shift 2
    ;;
    -rl|--resultslocation)
      # report location
      resultslocation="$2"
      if ! [ -f "$resultslocation" ] ; then
        echo "Result location $resultslocation does not exist."
        echo "Creating result location $resultslocation"
        mkdir -p $resultslocation
      fi
      echo "resultslocation = "$resultslocation
      shift 2
    ;;
    -rn|--reportname)
      # report name
      reportname="$2"
      echo "reportname = "$reportname
      shift 2
    ;;
    -ht|--hiptest)
      # report name
      hiptest="$2"
      echo "hiptest = "$hiptest
      shift 2
    ;;
     -htcf|--hiptestconfigfile)
      # report name
      hiptestconfigfile="$2"
      echo "hiptestconfigfile = "$hiptestconfigfile
      shift 2
    ;;
    -h|--help)
      echo "-tl|--testlocation = valid location of feature directory"
      echo "-t|--tags = scenario tags in the feature file"
      echo "if no tag is specificed then all tests will run"
      echo "to run all login tests: --tags=hollard-login"
      echo "to run valid valid-account: --tags=valid-account"
      echo "to run valid valid-account: --tags=vaild-username-invalid-password"
      echo "to run valid valid-account: --tags=invalid-username-valid-password"
      echo "to run valid valid-account: --tags=invalid-username-invalid-password"
      echo "to run valid valid-account: --tags=password-length-message"
      echo "to run valid valid-account: --tags=password-enter-a-value"
      echo "-j|--junit = true ; -j|--junit = false"
      echo "-rl|--reportlocation = valid location to which reports are written"
      echo "if no report location is specified or if the report location is invalid then the report location defaults to //usr/local/behave/reports/"
      exit 0
    ;;
    -*|--*)
      # Unknown option found
      ErrorMessage "Unknown option $1."
      exit -1
    ;;
    *)
      break
    ;;
  esac
done

main_method
