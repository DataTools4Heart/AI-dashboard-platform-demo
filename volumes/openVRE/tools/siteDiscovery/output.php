<?php

require __DIR__."/../../../config/bootstrap.php";

$data = explode ("_", $_REQUEST['execution']);

$files = $GLOBALS['filesCol']->findOne(
    ['_id' => $_REQUEST['execution']],
    ['files' => 1, '_id' => 0]
);
$outputFiles = [];
foreach ($files['files'] as $fileId) {
    $outputFiles[] = $GLOBALS['filesCol']->findOne(
        ['_id' => $fileId]
    );
}
$path = $GLOBALS['shared']."userdata/".$outputFiles[0]['path'];
$sites = json_decode(file_get_contents($path), $associative=True);

$progress = ['pending', 'testing', 'active'];
$types = ['comp'=> 'Computational', 'data'=> 'Data', 'both'=>'Data & Computational'];
$status = ['inactive', 'active'];

require $GLOBALS['root']."/public/htmlib/header.inc.php";
?>

<body class="page-header-fixed page-sidebar-closed-hide-logo page-content-white page-container-bg-solid page-sidebar-fixed">
    <div class="page-wrapper">

    <?php require $GLOBALS['root']."/public/htmlib/top.inc.php"; ?>
    <?php require $GLOBALS['root']."/public/htmlib/menu.inc.php"; ?>

    <!-- BEGIN CONTENT -->
        <div class="page-content-wrapper">
        <!-- BEGIN CONTENT BODY -->
            <div class="page-content">
            <!-- BEGIN PAGE HEADER-->
            <!-- BEGIN PAGE TITLE-->
                <h1 class="page-title">
                    <a href="javascript:;" target="_blank"><img src="assets/layouts/layout/img/icon.png" width=100></a>
                        <?=$GLOBALS['AppPrefix']?> Sites and Status
                </h1>
            <!-- END PAGE TITLE-->
            <!-- END PAGE HEADER-->
                <div class="row">
                      <div class="col-md-12">
                        <!-- BEGIN EXAMPLE TABLE PORTLET-->
                            <div class="portlet light portlet-fit bordered">
                                <div class="portlet-title">
                                    <div class="caption">
                                        <i class="icon-share font-red-sunglo hide"></i>
                                        <span class="caption-subject font-dark bold"><?=$GLOBALS['AppPrefix']?> sites. Status and available resources</span>
                                    </div>
                                </div>
                                <div class="portlet-body">
                                    <table class="table table-striped table-hover table-bordered" id="table-sites">
                                        <thead>
                                            <tr>
                                                <th> Site Id </th>
                                                <th> Full Name </th>
                                                <th> Type </th>
                                                <th> Progress </th>
                                                <th> Status </th>
                                                <th> Resources </th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <!-- process and display each result row -->
                                    <?php foreach ($sites as $obj) {?>
                                            <tr>
                                                <td> <?= $obj["_id"] ?> </td>
                                                <td> <?= $obj["name"] ?> </td>
                                                <td> <?= $types[$obj["type"]] ?> </td>
                                                <td> <?= $progress[$obj["progress"]] ?> </td>
                                                <td> <?= $status[$obj["status"]] ?> </td>
			                                    <td>
                                                    CPUs: <?= $obj["cpu_count"]?> (<?=$obj['cpu_percent']?>%),
                                                    GPUs <?= $obj['gpu_count']?>,
                                                    Free RAM: <?= $obj['memory']['available']?>/<?= $obj['memory']['total']?>,
                                                    Conn: <?=$obj["outbound_connectivity"]?>
                                                </td>
                                            </tr>
                                    <?php } ?>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        <!-- END EXAMPLE TABLE PORTLET-->
                        </div>
                    </div>
                </div>
            <!-- END CONTENT BODY -->
            </div>
        <!-- END CONTENT -->
<?php
require $GLOBALS['root']."/public/htmlib/footer.inc.php";
require $GLOBALS['root']."/public/htmlib/js.inc.php";
