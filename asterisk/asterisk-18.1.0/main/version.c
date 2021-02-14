/*
 * version.c
 * Automatically generated
 */

#include "asterisk.h"

#include "asterisk/ast_version.h"

static const char asterisk_version[] = "18.1.0";

static const char asterisk_version_num[] = "180100";

static const char asterisk_build_opts[] = "BUILD_NATIVE, OPTIONAL_API";

const char *ast_get_version(void)
{
	return asterisk_version;
}

const char *ast_get_version_num(void)
{
	return asterisk_version_num;
}

const char *ast_get_build_opts(void)
{
	return asterisk_build_opts;
}

