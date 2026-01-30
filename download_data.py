from roboflow import Roboflow

rf = Roboflow(api_key="DFvGq8iznhx4vFr0TpS1")

project = rf.workspace("roboflow-universe-projects").project("coco-2017")
dataset = project.version(1).download("yolov8")
